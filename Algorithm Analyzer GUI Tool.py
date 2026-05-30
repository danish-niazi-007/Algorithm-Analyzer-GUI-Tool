import customtkinter as ctk
import random
import time
from tkinter import Canvas

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AlgorithmAnalyzer(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Algorithm Analyzer GUI")
        self.geometry("900x650")
        
        self.tabview = ctk.CTkTabview(self, width=850, height=600)
        self.tabview.pack(padx=20, pady=20)
        
        self.tab_heap = self.tabview.add("Heap Sort")
        self.tab_kruskal = self.tabview.add("Kruskal's Algorithm")
        
        self.setup_heap_sort_ui()
        self.setup_kruskal_ui()
        
    def setup_heap_sort_ui(self):
        self.heap_data = []
        self.heap_canvas = Canvas(self.tab_heap, width=800, height=400, bg="#2b2b2b", highlightthickness=0)
        self.heap_canvas.pack(pady=20)
        
        btn_frame = ctk.CTkFrame(self.tab_heap)
        btn_frame.pack(pady=10)
        
        self.btn_gen_heap = ctk.CTkButton(btn_frame, text="Generate Array", command=self.generate_heap_data)
        self.btn_gen_heap.grid(row=0, column=0, padx=10)
        
        self.btn_sort_heap = ctk.CTkButton(btn_frame, text="Run Heap Sort", command=self.run_heap_sort)
        self.btn_sort_heap.grid(row=0, column=1, padx=10)
        
        self.generate_heap_data()

    def generate_heap_data(self):
        self.heap_data = [random.randint(10, 380) for _ in range(50)]
        self.draw_heap_data(["#1f6aa5" for _ in range(len(self.heap_data))])

    def draw_heap_data(self, color_array):
        self.heap_canvas.delete("all")
        c_width = 800
        c_height = 400
        x_width = c_width / (len(self.heap_data) + 1)
        offset = 10
        spacing = 2
        
        for i, height in enumerate(self.heap_data):
            x0 = i * x_width + offset + spacing
            y0 = c_height - height
            x1 = (i + 1) * x_width + offset
            y1 = c_height
            self.heap_canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i], outline="")
        self.update_idletasks()

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and self.heap_data[i] < self.heap_data[l]:
            largest = l
        if r < n and self.heap_data[largest] < self.heap_data[r]:
            largest = r
            
        if largest != i:
            self.heap_data[i], self.heap_data[largest] = self.heap_data[largest], self.heap_data[i]
            colors = ["#1f6aa5"] * len(self.heap_data)
            colors[i] = "#e05260"
            colors[largest] = "#e05260"
            self.draw_heap_data(colors)
            time.sleep(0.05)
            self.heapify(n, largest)

    def run_heap_sort(self):
        self.btn_gen_heap.configure(state="disabled")
        self.btn_sort_heap.configure(state="disabled")
        n = len(self.heap_data)
        
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
            
        for i in range(n - 1, 0, -1):
            self.heap_data[i], self.heap_data[0] = self.heap_data[0], self.heap_data[i]
            colors = ["#1f6aa5"] * len(self.heap_data)
            for j in range(i, n):
                colors[j] = "#2fa572"
            colors[0] = "#e05260"
            self.draw_heap_data(colors)
            time.sleep(0.05)
            self.heapify(i, 0)
            
        self.draw_heap_data(["#2fa572"] * len(self.heap_data))
        self.btn_gen_heap.configure(state="normal")
        self.btn_sort_heap.configure(state="normal")

    def setup_kruskal_ui(self):
        self.nodes = []
        self.edges = []
        self.k_canvas = Canvas(self.tab_kruskal, width=800, height=400, bg="#2b2b2b", highlightthickness=0)
        self.k_canvas.pack(pady=20)
        
        btn_frame = ctk.CTkFrame(self.tab_kruskal)
        btn_frame.pack(pady=10)
        
        self.btn_gen_graph = ctk.CTkButton(btn_frame, text="Generate Graph", command=self.generate_graph)
        self.btn_gen_graph.grid(row=0, column=0, padx=10)
        
        self.btn_run_kruskal = ctk.CTkButton(btn_frame, text="Run Kruskal's", command=self.run_kruskal)
        self.btn_run_kruskal.grid(row=0, column=1, padx=10)
        
        self.generate_graph()

    def generate_graph(self):
        self.k_canvas.delete("all")
        self.nodes = []
        self.edges = []
        num_nodes = 8
        
        for _ in range(num_nodes):
            x = random.randint(50, 750)
            y = random.randint(50, 350)
            self.nodes.append((x, y))
            
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if random.random() > 0.4:
                    x1, y1 = self.nodes[i]
                    x2, y2 = self.nodes[j]
                    weight = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5 / 10)
                    self.edges.append((weight, i, j))
                    
        self.draw_graph([])

    def draw_graph(self, mst_edges):
        self.k_canvas.delete("all")
        
        for weight, u, v in self.edges:
            x1, y1 = self.nodes[u]
            x2, y2 = self.nodes[v]
            is_mst = (u, v) in mst_edges or (v, u) in mst_edges
            color = "#2fa572" if is_mst else "#555555"
            width = 3 if is_mst else 1
            self.k_canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
            
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            self.k_canvas.create_text(mx, my, text=str(weight), fill="white", font=("Arial", 10))
            
        for i, (x, y) in enumerate(self.nodes):
            self.k_canvas.create_oval(x-15, y-15, x+15, y+15, fill="#1f6aa5", outline="white")
            self.k_canvas.create_text(x, y, text=str(i), fill="white", font=("Arial", 12, "bold"))
            
        self.update_idletasks()

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def run_kruskal(self):
        self.btn_gen_graph.configure(state="disabled")
        self.btn_run_kruskal.configure(state="disabled")
        
        mst = []
        self.edges = sorted(self.edges, key=lambda item: item[0])
        parent = []
        rank = []
        
        for node in range(len(self.nodes)):
            parent.append(node)
            rank.append(0)
            
        for edge in self.edges:
            weight, u, v = edge
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x != y:
                mst.append((u, v))
                self.apply_union(parent, rank, x, y)
                self.draw_graph(mst)
                time.sleep(0.5)
                
        self.btn_gen_graph.configure(state="normal")
        self.btn_run_kruskal.configure(state="normal")

if __name__ == "__main__":
    app = AlgorithmAnalyzer()
    app.mainloop()