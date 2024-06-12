import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class PDV:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema PDV")
        self.root.geometry("400x500")
        self.root.configure(bg="lightblue")

        self.products = {
            "001": {"name": "Produto 1", "price": 10.00},
            "002": {"name": "Produto 2", "price": 15.00},
            "003": {"name": "Produto 3", "price": 20.00},
        }

        self.cart = []
        self.total = 0.0

        self.create_widgets()

    def create_widgets(self):
        self.frame_top = tk.Frame(self.root, bg="lightblue")
        self.frame_top.pack(pady=10)

        self.label_code = tk.Label(self.frame_top, text="Código do Produto:", bg="lightblue", font=("Arial", 12))
        self.label_code.grid(row=0, column=0, padx=5)
        self.entry_code = tk.Entry(self.frame_top, font=("Arial", 12))
        self.entry_code.grid(row=0, column=1, padx=5)
        self.entry_code.bind('<Return>', lambda event: self.add_to_cart())

        self.btn_add = tk.Button(self.frame_top, text="Adicionar ao Carrinho", command=self.add_to_cart, font=("Arial", 12), bg="green", fg="white")
        self.btn_add.grid(row=0, column=2, padx=5)

        self.frame_cart = tk.Frame(self.root, bg="lightblue")
        self.frame_cart.pack(pady=10)

        self.cart_display = tk.Text(self.frame_cart, height=10, width=50, font=("Arial", 12))
        self.cart_display.pack()

        self.label_total = tk.Label(self.root, text="Total: R$ 0.00", bg="lightblue", font=("Arial", 16, "bold"))
        self.label_total.pack(pady=10)

        self.btn_finalize = tk.Button(self.root, text="Finalizar Compra", command=self.finalize_purchase, font=("Arial", 12), bg="blue", fg="white")
        self.btn_finalize.pack(pady=10)

    def add_to_cart(self):
        code = self.entry_code.get()
        if code in self.products:
            product = self.products[code]
            self.cart.append(product)
            self.total += product["price"]
            self.update_cart_display()
        else:
            messagebox.showerror("Erro", "Código de produto inválido")

    def update_cart_display(self):
        self.cart_display.delete(1.0, tk.END)
        for item in self.cart:
            self.cart_display.insert(tk.END, f"{item['name']} - R$ {item['price']:.2f}\n")
        self.label_total.config(text=f"Total: R$ {self.total:.2f}")

    def finalize_purchase(self):
        if not self.cart:
            messagebox.showwarning("Aviso", "Carrinho vazio")
            return

        messagebox.showinfo("Compra Finalizada", f"Total a pagar: R$ {self.total:.2f}")
        self.cart.clear()
        self.total = 0.0
        self.update_cart_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = PDV(root)
    root.mainloop()
