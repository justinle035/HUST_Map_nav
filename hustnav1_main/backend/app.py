from flask import Flask, request, jsonify
from map_parser import Graph
from dijkstra import dijkstra
import json
import folium
import os

app = Flask(__name__, static_folder='static')

# Khởi tạo và phân tích dữ liệu OSM
graph = Graph()
graph.parse_osm(r"C:\Users\Acer\HUST\DSA\hustnav1_main\backend\data\hust.osm")
nodes, edges = graph.get_graph()

# Load tên địa điểm → tọa độ từ file locations.json
with open(r"C:\Users\Acer\HUST\DSA\hustnav1_main\backend\locations.json", encoding="utf-8") as f:
    locations = json.load(f)

@app.route('/')
def home():
    return open(r"C:\Users\Acer\HUST\DSA\hustnav1_main\templates\index.html", encoding='utf-8')

@app.route('/find_route', methods=['GET'])
def find_route():
    start = request.args.get('start')
    end = request.args.get('end')

    # Kiểm tra tên địa điểm hợp lệ
    if start not in locations or end not in locations:
        return jsonify({"error": "Tên địa điểm không hợp lệ."}), 400

    # Lấy node gần nhất từ file locations
    start_node_info = locations[start]
    end_node_info = locations[end]
    start_node_id = start_node_info['node_id']
    end_node_id = end_node_info['node_id']

    print(f"Start Node ID: {start_node_id}, End Node ID: {end_node_id}")

    # Kiểm tra tồn tại cạnh
    if start_node_id not in edges or not edges[start_node_id]:
        return jsonify({"error": f"Start node {start_node_id} không có kết nối."}), 400
    if end_node_id not in edges or not edges[end_node_id]:
        return jsonify({"error": f"End node {end_node_id} không có kết nối."}), 400

    # Chạy thuật toán Dijkstra
    dist, path = dijkstra(start_node_id, end_node_id, nodes, edges)
    print(f"Distance: {dist}, Path: {path}")

    #if dist == float('inf') or not path:
       # return jsonify({"error": "Không tìm được đường đi."}), 404

    # Vẽ bản đồ bằng folium
    create_route_map(path, nodes)

    return jsonify({
        'distance': dist,
        'path': path,
        'map_url': '/map'
    })

@app.route('/map')
def show_map():
    return open('save/map.html', encoding='utf-8').read()

def create_route_map(path, nodes, output_path='save/map.html'):
    if not path:
        return

    start_coords = nodes[path[0]]
    fmap = folium.Map(location=start_coords, zoom_start=18)

    # Vẽ các node
    for node_id in path:
        lat, lon = nodes[node_id]
        folium.CircleMarker(
            location=(lat, lon),
            radius=4,
            color='blue',
            fill=True,
            fill_opacity=0.7,
            popup=f'Node ID: {node_id}'
        ).add_to(fmap)

    # Vẽ đường nối
    route_coords = [nodes[node_id] for node_id in path]
    folium.PolyLine(route_coords, color='red', weight=4).add_to(fmap)

    # Lưu bản đồ
    fmap.save(output_path)

if __name__ == '__main__':
    app.run(debug=True)
