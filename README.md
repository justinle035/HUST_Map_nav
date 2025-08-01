---

# HUST Map Shortest Path & Nearest Parking Finder

A Python-based web application to help users:

*  **Find the shortest path** between two locations on the Hanoi University of Science and Technology (HUST) campus map
*  **Locate the nearest parking lot** using Dijkstra’s algorithm

---

## Features

* Interactive web interface built with Flask
* Route visualization on a dynamic map
* Parking recommendation with shortest distance

---

## Requirements

* Python 3.x
* Flask-compatible environment
* Web browser (e.g., Chrome)
* Optional: VS Code or any code editor

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/knguyenz/hustnav1
cd hustnav1
```

> **Note:** This project uses **absolute paths** in `app.py`. You will need to **update them to your local machine paths** (see [Notes on File Paths](#-notes-on-file-paths)).

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the Flask server

```bash
cd backend
python app.py
```

The server will start at:
**[http://localhost:5000](http://localhost:5000)**

---

## Using the App

1. Open your browser and navigate to:
   **[http://localhost:5000](http://localhost:5000)**

2. To **find a route**:

   * Input start and destination (e.g., `C7` to `D8`)
   * Click **"Tìm đường" (Find route)**
   * Open `http://localhost:5000/map` to view the result

3. To **find the nearest parking lot**:

   * Input only the starting location
   * Click **"Tìm nhà xe gần nhất" (Find nearest parking)**
   * Open `http://localhost:5000/map` to view the route

---

## Notes on File Paths

Make sure to **manually update file paths** in `app.py`:

* `.osm` files
* `.json` data files
* `map.html` output

Use your system’s file explorer to locate correct paths.

---

## Test Cases

<img width="1914" height="921" alt="image" src="https://github.com/user-attachments/assets/d8fe4d0f-90dc-4284-84f4-eae63bcaed92" />
<img width="1215" height="843" alt="image" src="https://github.com/user-attachments/assets/87bc47e8-6ad6-460e-bfc1-d2608443fe9c" />
<img width="1616" height="733" alt="image" src="https://github.com/user-attachments/assets/f276e80c-3e9d-423c-92ce-ef04522a3dde" />


---

## Authors

Developed by **Group 5** from the *Data Structures & Algorithms* course at **Hanoi University of Science and Technology (HUST)**:

* Phan Khôi Nguyên
* Lê Bá Nhật Nguyên
* Đào Nguyên Minh Vũ

---
