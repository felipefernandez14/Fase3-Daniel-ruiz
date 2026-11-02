import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque
from datetime import datetime


# =====================================================================
# CLASE DE NEGOCIO / ABSTRACCIÓN DE DATOS (AffiliateDataStructure)
# =====================================================================
class AffiliateDataStructure:
    """
    Clase que almacena la información de cada afiliado y calcula
    su tarifa de afiliación.
    """
    def __init__(self, id_type: str, id_number: int, full_name: str,
                 current_income: float, employment_type: str,
                 desired_service: str, affiliation_fee: float,
                 affiliation_date: str):
        self.id_type = id_type
        self.id_number = id_number
        self.full_name = full_name
        self.current_income = current_income
        self.employment_type = employment_type
        self.desired_service = desired_service
        self.affiliation_fee = affiliation_fee
        self.affiliation_date = affiliation_date

    @staticmethod
    def calculate_fee(income: float, employment_type: str, service: str) -> float:
        """
        Calcula la tarifa de afiliación combinando la tarifa base (según
        ingresos y modalidad de empleo) más el recargo del servicio deseado.
        """
        base_fee = 0.0

        if employment_type == "Employee":
            if 1000000 <= income <= 2000000:
                base_fee = 45000
            elif 2000000 < income <= 3000000:
                base_fee = 60000
            elif 3000000 < income <= 4000000:
                base_fee = 75000
            elif 4000000 < income <= 5000000:
                base_fee = 90000
            elif income > 5000000:
                base_fee = 150000
            else:

                base_fee = 45000
        elif employment_type == "Independent":
            if 1000000 <= income <= 2000000:
                base_fee = 10000
            elif 2000000 < income <= 3000000:
                base_fee = 20000
            elif 3000000 < income <= 4000000:
                base_fee = 30000
            elif 4000000 < income <= 5000000:
                base_fee = 40000
            elif income > 5000000:
                base_fee = 80000
            else:
                base_fee = 10000

        additional_fee = 0.0
        if service == "Unemployment subsidy":
            additional_fee = 0.0
        elif service == "Park entry":
            additional_fee = 2500.0
        elif service == "Training course":
            additional_fee = 7500.0
        elif service == "Travel package":
            additional_fee = 10000.0
        elif service == "Preventive medicine":
            additional_fee = income * 0.10  

        return base_fee + additional_fee

    def to_tuple(self) -> tuple:
        """Retorna los atributos formateados para insertarlos en el Treeview."""
        return (
            self.id_type,
            self.id_number,
            self.full_name,
            f"${self.current_income:,.0f}",
            self.desired_service,
            self.employment_type,
            f"${self.affiliation_fee:,.0f}",
            self.affiliation_date
        )


# =====================================================================
# VENTANA DE INICIO DE SESIÓN (Login Window)
# =====================================================================
class LoginWindow:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Login — Compensándote")
        self.root.geometry("460x480")
        self.root.configure(bg="#2617AA")
        self.root.resizable(False, False)


        self.correct_password = "Caja"
        self.app_name = "Fase3DanielRuiz"
        self.student_name = "Danie Felipe Ruiz Fernandez"
        self.course_info = "ESTRUCTURAS DE DATOS - (301305A_2204)"
        self.group_info = "150"
        self.current_date = datetime.now().strftime("%B %d, %Y")

        self._create_menu()
        self._create_widgets()

    def _create_menu(self):
        """Crea la barra de menú superior con la opción 'About' (Acerca de)."""
        menubar = tk.Menu(self.root)
        menubar.add_command(label="About", command=self.show_about)
        self.root.config(menu=menubar)

    def _create_widgets(self):
        """Construye los controles visuales de la ventana de Login."""
        
        tk.Label(
            self.root, text="Compensándote", font=("Segoe UI", 22, "bold"),
            fg="#F3F3F3", bg="#3327B3", highlightbackground="#1C155A",
             highlightthickness=2, padx=19, pady=12
        ).pack(pady=(25, 2))

        tk.Label(
            self.root, text="Family Compensation Fund — Affiliation Control",
            font=("Segoe UI", 10), fg="#F3F3F3", bg="#3327B3",highlightbackground="#1C155A",
             highlightthickness=2, padx=19, pady=12
        ).pack(pady=(0, 15))

        
        info_frame = tk.Frame(
            self.root, bg="#3327B3", highlightbackground="#1C155A",
            highlightthickness=2, padx=19, pady=1
        )
        info_frame.pack(padx=35, fill="x")

        labels = [
            ("Application:", self.app_name),
            ("Student:", self.student_name),
            ("Course:", self.course_info),
            ("Date:", self.current_date)
        ]
        for row_idx, (title, val) in enumerate(labels):
            tk.Label(
                info_frame, text=title, font=("Segoe UI", 9, "bold"),
                fg="#A09FAC", bg="#463BC0", anchor="w", width=12
            ).grid(row=row_idx, column=0, sticky="w", pady=2)
            tk.Label(
                info_frame, text=val, font=("Segoe UI", 9),
                fg="#ffffff", bg="#463BC0", anchor="w",
                
            ).grid(row=row_idx, column=1, sticky="w", pady=2)

        pwd_frame = tk.Frame(self.root, bg="#463BC0", highlightbackground="#1C155A",
            highlightthickness=2, padx=10, pady=1
                             )
        pwd_frame.pack(padx=35, pady=(20, 5), fill="x")

        tk.Label(
            pwd_frame, text="Password", font=("Segoe UI", 10, "bold"),
            fg="#A09FAC", bg="#382BB1"
        ).pack(anchor="w")

        self.password_var = tk.StringVar()
        self.txt_password = tk.Entry(
            pwd_frame, textvariable=self.password_var, show="*",
            font=("Segoe UI", 12), bg="#382BB1", fg="#ffffff",
            insertbackground="#ffffff", relief="solid", bd=1
        )
        self.txt_password.pack(fill="x", pady=(5, 2), ipady=6)
        self.txt_password.focus()

        tk.Label(
            pwd_frame, text="Password masked ( '*' )",
            font=("Segoe UI", 8), fg="#6c757d", bg="#382BB1"
        ).pack(anchor="w")

        btn_frame = tk.Frame(self.root, bg="#2617AA")
        btn_frame.pack(padx=35, pady=20, fill="x")

        btn_login = tk.Button(
            btn_frame, text="Login →", font=("Segoe UI", 10, "bold"),
            bg="#382BB1", fg="#000000", activebackground="#382BB1",
            relief="flat", cursor="hand2", command=self.login
        )
        btn_login.pack(side="left", expand=True, fill="x", padx=(0, 8), ipady=8)

        btn_exit = tk.Button(
            btn_frame, text="Exit", font=("Segoe UI", 10, "bold"),
            bg="#e63946", fg="#ffffff", activebackground="#d62828",
            relief="flat", cursor="hand2", command=self.exit_app
        )
        btn_exit.pack(side="right", expand=True, fill="x", padx=(8, 0), ipady=8)

    def show_about(self):

        about_text = (
            f"Course: {self.course_info}\n"
            f"Student: {self.student_name}\n"
            f"Collaborative Group: {self.group_info}\n"
            f"UNAD - ECBTI - Systems Engineering\n"
            f"Date: {self.current_date}"
        )
        messagebox.showinfo("About", about_text)

    def login(self):
        """Valida que la contraseña sea 'Caja' y abre el formulario principal."""
        if self.password_var.get() == self.correct_password:
            self.root.destroy()  
            main_root = tk.Tk()
            AffiliationControlWindow(main_root, self.student_name, self.course_info)
            main_root.mainloop()
        else:
            messagebox.showerror("Access Denied", "Incorrect password. Please try again.")
            self.password_var.set("")
            self.txt_password.focus()

    def exit_app(self):
        """Finaliza la ejecución de la aplicación."""
        self.root.destroy()


# =====================================================================
# VENTANA PRINCIPAL DE INGRESO DE DATOS (Affiliation Control Window)
# =====================================================================
class AffiliationControlWindow:
    def __init__(self, root: tk.Tk, student_name: str, course_info: str):
        self.root = root
        self.root.title("Caja Compensándote - Control de Afiliados")
        self.root.geometry("1180x680")
        self.root.state("zoomed")
        self.root.configure(bg="#2617AA")

        self.student_name = student_name
        self.course_info = course_info

        # Estructuras de datos en memoria principal:
        # 1. Pila (Stack) implementada con collections.deque
        self.stack_data = deque()
        # 2. Cola (Queue) implementada con collections.deque
        self.queue_data = deque()
        # 3. Lista (List) implementada con list nativa de Python
        self.list_data = []

        self._build_ui()
        self.update_fee_calculation()

    def _build_ui(self):
        """Construye el panel izquierdo de formulario y derecho de Treeview."""

        header = tk.Frame(self.root, bg="#3327B3", pady=10, padx=15)
        header.pack(fill="x")

        tk.Label(
            header, text="Compensándote — Affiliation Control",
            font=("Segoe UI", 14, "bold"), fg="#00b4d8", bg="#3327B3"
        ).pack(side="left")

        tk.Label(
            header, text=f"{self.student_name}  |  {self.course_info}",
            font=("Segoe UI", 9), fg="#b0c4de", bg="#3327B3"
        ).pack(side="right")

        main_frame = tk.Frame(self.root, bg="#2617AA")
        main_frame.pack(fill="both", expand=True, padx=12, pady=10)

        left_panel = tk.Frame(
            main_frame, bg="#3B3197", width=330, padx=15, pady=12,
            highlightbackground="#0C0A1F", highlightthickness=1
        )
        left_panel.pack(side="left", fill="y", padx=(0, 10))
        left_panel.pack_propagate(False)

        tk.Label(
            left_panel, text="1. Identification", font=("Segoe UI", 10, "bold"),
            fg="#00b4d8", bg="#3B3197"
        ).pack(anchor="w", pady=(0, 5))

        tk.Label(left_panel, text="ID Type:", fg="#ffffff", bg="#3B3197", font=("Segoe UI", 9)).pack(anchor="w")
        self.id_type_var = tk.StringVar(value="CC")
        self.cmb_id_type = ttk.Combobox(
            left_panel, textvariable=self.id_type_var,
            values=["CC", "CE", "NUIP", "PAS"], state="readonly"
        )
        self.cmb_id_type.pack(fill="x", pady=(2, 8))

        tk.Label(left_panel, text="ID Number (digits only):", fg="#ffffff", bg="#3B3197", font=("Segoe UI", 9)).pack(anchor="w")
        self.id_number_var = tk.StringVar()
        vcmd_num = (self.root.register(self._validate_numbers), "%P")
        self.txt_id_number = tk.Entry(
            left_panel, textvariable=self.id_number_var, validate="key",
            validatecommand=vcmd_num, bg="#0d2137", fg="#ffffff", insertbackground="#ffffff"
        )
        self.txt_id_number.pack(fill="x", pady=(2, 8), ipady=3)

        tk.Label(left_panel, text="Full Name (letters only):", fg="#ffffff", bg="#3B3197", font=("Segoe UI", 9)).pack(anchor="w")
        self.full_name_var = tk.StringVar()
        vcmd_let = (self.root.register(self._validate_letters), "%P")
        self.txt_full_name = tk.Entry(
            left_panel, textvariable=self.full_name_var, validate="key",
            validatecommand=vcmd_let, bg="#0d2137", fg="#ffffff", insertbackground="#ffffff"
        )
        self.txt_full_name.pack(fill="x", pady=(2, 10), ipady=3)

        tk.Label(
            left_panel, text="2. Economic Data", font=("Segoe UI", 10, "bold"),
            fg="#00b4d8", bg="#3B3197"
        ).pack(anchor="w", pady=(4, 5))

        tk.Label(left_panel, text="Current Income ($):", fg="#ffffff", bg="#3B3197", font=("Segoe UI", 9)).pack(anchor="w")
        self.income_var = tk.StringVar()
        self.income_var.trace_add("write", lambda *args: self.update_fee_calculation())
        self.txt_income = tk.Entry(
            left_panel, textvariable=self.income_var, validate="key",
            validatecommand=vcmd_num, bg="#0d2137", fg="#ffffff", insertbackground="#ffffff"
        )
        self.txt_income.pack(fill="x", pady=(2, 8), ipady=3)

        tk.Label(left_panel, text="Employment Type:", fg="#ffffff", bg="#3B3197", font=("Segoe UI", 9)).pack(anchor="w")
        self.employment_var = tk.StringVar(value="Employee")
        rb_frame = tk.Frame(left_panel, bg="#3B3197")
        rb_frame.pack(fill="x", pady=(2, 8))
        tk.Radiobutton(
            rb_frame, text="Employee", variable=self.employment_var, value="Employee",
            command=self.update_fee_calculation, bg="#3B3197", fg="#ffffff",
            selectcolor="#0d2137", activebackground="#3B3197"
        ).pack(side="left", padx=(0, 15))
        tk.Radiobutton(
            rb_frame, text="Independent", variable=self.employment_var, value="Independent",
            command=self.update_fee_calculation, bg="#3B3197", fg="#ffffff",
            selectcolor="#0d2137", activebackground="#3B3197"
        ).pack(side="left")

        tk.Label(left_panel, text="Desired Service:", fg="#ffffff", bg="#3B3197", font=("Segoe UI", 9)).pack(anchor="w")
        self.service_var = tk.StringVar(value="Unemployment subsidy")
        self.cmb_service = ttk.Combobox(
            left_panel, textvariable=self.service_var, state="readonly",
            values=[
                "Unemployment subsidy",
                "Park entry",
                "Training course",
                "Travel package",
                "Preventive medicine"
            ]
        )
        self.cmb_service.pack(fill="x", pady=(2, 8))
        self.cmb_service.bind("<<ComboboxSelected>>", lambda e: self.update_fee_calculation())

        tk.Label(left_panel, text="Affiliation Fee ($) — read only:", fg="#ffffff", bg="#3B3197", font=("Segoe UI", 9)).pack(anchor="w")
        self.fee_var = tk.StringVar(value="0")
        self.txt_fee = tk.Entry(
            left_panel, textvariable=self.fee_var, state="readonly",
            readonlybackground="#e9ecef", fg="#000000", font=("Segoe UI", 9, "bold")
        )
        self.txt_fee.pack(fill="x", pady=(2, 10), ipady=3)

        tk.Label(
            left_panel, text="3. Affiliation Date (dd/mm/yyyy)",
            font=("Segoe UI", 10, "bold"), fg="#00b4d8", bg="#3B3197"
        ).pack(anchor="w", pady=(2, 4))

        date_frame = tk.Frame(left_panel, bg="#3B3197")
        date_frame.pack(fill="x", pady=(0, 10))

        now = datetime.now()
        self.day_var = tk.StringVar(value=f"{now.day:02d}")
        self.month_var = tk.StringVar(value=f"{now.month:02d}")
        self.year_var = tk.StringVar(value=str(now.year))

        for idx, (lbl, var, from_, to_, width) in enumerate([
            ("Day", self.day_var, 1, 31, 5),
            ("Month", self.month_var, 1, 12, 5),
            ("Year", self.year_var, 2000, 2035, 7)
        ]):
            col_f = tk.Frame(date_frame, bg="#3B3197")
            col_f.pack(side="left", padx=(0, 10))
            tk.Label(col_f, text=lbl, fg="#b0c4de", bg="#3B3197", font=("Segoe UI", 8)).pack(anchor="w")
            tk.Spinbox(
                col_f, from_=from_, to=to_, textvariable=var, width=width,
                format="%02.0f" if width == 5 else "%4.0f", state="readonly"
            ).pack()

        tk.Label(
            left_panel, text="4. Data Structure & Report",
            font=("Segoe UI", 10, "bold"), fg="#00b4d8", bg="#3B3197"
        ).pack(anchor="w", pady=(4, 4))

        tk.Label(left_panel, text="View Structure (Pila / Cola / Lista):", fg="#ffffff", bg="#3B3197", font=("Segoe UI", 9)).pack(anchor="w")
        self.structure_var = tk.StringVar(value="Stack")
        self.cmb_structure = ttk.Combobox(
            left_panel, textvariable=self.structure_var,
            values=["Stack", "Queue", "List"], state="readonly"
        )
        self.cmb_structure.pack(fill="x", pady=(2, 8))
        self.cmb_structure.bind("<<ComboboxSelected>>", lambda e: self.refresh_treeview())

        tk.Label(left_panel, text="Report (read only):", fg="#ffffff", bg="#3B3197", font=("Segoe UI", 9)).pack(anchor="w")
        self.report_var = tk.StringVar(value="Click 'Report' to calculate")
        self.txt_report = tk.Entry(
            left_panel, textvariable=self.report_var, state="readonly",
            readonlybackground="#e9ecef", fg="#000000", font=("Segoe UI", 9, "bold")
        )
        self.txt_report.pack(fill="x", pady=(2, 5), ipady=3)

        right_panel = tk.Frame(main_frame, bg="#3B3197")
        right_panel.pack(side="right", fill="both", expand=True)

        self.lbl_tree_title = tk.Label(
            right_panel, text="Stack — Registered Affiliates",
            font=("Segoe UI", 11, "bold"), fg="#00b4d8", bg="#3B3197"
        )
        self.lbl_tree_title.pack(anchor="w", pady=(0, 6))

        tree_frame = tk.Frame(right_panel, bg="#3B3197")
        tree_frame.pack(fill="both", expand=True)

        columns = (
            "id_type", "id_number", "full_name", "income",
            "service", "employment", "fee", "date"
        )
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

        headers = {
            "id_type": ("ID Type", 65),
            "id_number": ("ID Number", 95),
            "full_name": ("Full Name", 150),
            "income": ("Income ($)", 95),
            "service": ("Service", 145),
            "employment": ("Employment", 95),
            "fee": ("Fee ($)", 85),
            "date": ("Date", 85)
        }
        for col, (text, width) in headers.items():
            self.tree.heading(col, text=text)
            self.tree.column(col, width=width, anchor="center")

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        btn_bar = tk.Frame(right_panel, bg="#3B3197", pady=10)
        btn_bar.pack(fill="x")

        buttons = [
            ("Register", "#00b4d8", "#000000", self.register),
            ("Delete", "#e63946", "#ffffff", self.delete),
            ("Report", "#2ec4b6", "#000000", self.generate_report),
            ("Clear", "#f4a261", "#000000", self.clear_fields),
            ("Exit", "#1d3557", "#ffffff", self.exit_app)
        ]
        for text, bg_col, fg_col, cmd in buttons:
            tk.Button(
                btn_bar, text=text, font=("Segoe UI", 10, "bold"),
                bg=bg_col, fg=fg_col, relief="flat", cursor="hand2",
                command=cmd
            ).pack(side="left", expand=True, fill="x", padx=4, ipady=8)

    # =================================================================
    # MÉTODOS DE VALIDACIÓN Y CÁLCULO DE TARIFA
    # =================================================================
    def _validate_numbers(self, new_value: str) -> bool:
        """Valida que solo se ingresen números enteros positivos."""
        return new_value == "" or new_value.isdigit()

    def _validate_letters(self, new_value: str) -> bool:
        """Valida que solo se ingresen letras y espacios."""
        if new_value == "":
            return True
        return all(char.isalpha() or char.isspace() for char in new_value)

    def update_fee_calculation(self):
        """Calcula automáticamente la tarifa cuando cambian ingresos, empleo o servicio."""
        income_str = self.income_var.get().strip()
        if not income_str:
            self.fee_var.set("0")
            return
        income = float(income_str)
        fee = AffiliateDataStructure.calculate_fee(
            income, self.employment_var.get(), self.service_var.get()
        )
        self.fee_var.set(f"{fee:.0f}")

    # =================================================================
    # MÉTODOS DE LAS ACCIONES DEL FORMULARIO (Requerimientos 5 al 9)
    # =================================================================
    def register(self):
        """
        Requisito 5: Valida los campos obligatorios e inserta el afiliado
        en la estructura seleccionada respetando su comportamiento:
        Pila (apilar), Cola (encolar) o Lista (agregar al final).
        """
        id_num_str = self.id_number_var.get().strip()
        name_str = self.full_name_var.get().strip()
        income_str = self.income_var.get().strip()

        if not id_num_str or not name_str or not income_str:
            messagebox.showwarning(
                "Validation Error",
                "All fields (ID Number, Full Name, and Current Income) are required."
            )
            return

        id_num = int(id_num_str)
        income = float(income_str)
        fee = float(self.fee_var.get())
        date_str = f"{int(self.day_var.get()):02d}/{int(self.month_var.get()):02d}/{self.year_var.get()}"

        new_affiliate = AffiliateDataStructure(
            id_type=self.id_type_var.get(),
            id_number=id_num,
            full_name=name_str,
            current_income=income,
            employment_type=self.employment_var.get(),
            desired_service=self.service_var.get(),
            affiliation_fee=fee,
            affiliation_date=date_str
        )

        structure = self.structure_var.get()
        if structure == "Stack":

            self.stack_data.appendleft(new_affiliate)
        elif structure == "Queue":

            self.queue_data.append(new_affiliate)
        elif structure == "List":

            self.list_data.append(new_affiliate)

        self.refresh_treeview()
        messagebox.showinfo("Success", f"Affiliate registered in {structure} successfully.")

    def delete(self):

        structure = self.structure_var.get()

        if structure == "Stack":
            if not self.stack_data:
                messagebox.showwarning("Empty Stack", "There are no records in the Stack to pop.")
                return
            target = self.stack_data[0]
            confirm = messagebox.askyesno(
                "Confirm Delete (Stack - Pop)",
                f"Do you want to pop the last registered affiliate from the Stack?\n\n"
                f"ID: {target.id_number} - {target.full_name}"
            )
            if confirm:
                self.stack_data.popleft()
                self.refresh_treeview()
                messagebox.showinfo("Deleted", "Top record popped from the Stack.")

        elif structure == "Queue":
            if not self.queue_data:
                messagebox.showwarning("Empty Queue", "There are no records in the Queue to dequeue.")
                return
            target = self.queue_data[0]
            confirm = messagebox.askyesno(
                "Confirm Delete (Queue - Dequeue)",
                f"Do you want to dequeue the first registered affiliate from the Queue?\n\n"
                f"ID: {target.id_number} - {target.full_name}"
            )
            if confirm:
                self.queue_data.popleft()
                self.refresh_treeview()
                messagebox.showinfo("Deleted", "First record dequeued from the Queue.")

        elif structure == "List":
            if not self.list_data:
                messagebox.showwarning("Empty List", "There are no records in the List.")
                return

            search_id_str = self.id_number_var.get().strip()
            if not search_id_str:
                messagebox.showwarning(
                    "ID Required",
                    "To delete from the List, please type the affiliate's ID Number first."
                )
                self.txt_id_number.focus()
                return

            search_id = int(search_id_str)
            found_affiliate = None
            for item in self.list_data:
                if item.id_number == search_id:
                    found_affiliate = item
                    break

            if not found_affiliate:
                messagebox.showerror(
                    "Not Found",
                    f"No affiliate found with ID Number {search_id} in the List."
                )
                return

            confirm = messagebox.askyesno(
                "Confirm Delete (List)",
                f"Affiliate found:\nID: {found_affiliate.id_number} - {found_affiliate.full_name}\n\n"
                f"Do you want to remove this record from the List?"
            )
            if confirm:
                self.list_data.remove(found_affiliate)
                self.refresh_treeview()
                messagebox.showinfo("Deleted", "Affiliate removed from the List.")

    def generate_report(self):

        structure = self.structure_var.get()

        if structure == "Stack":
            total_fees = sum(item.affiliation_fee for item in self.stack_data)
            self.report_var.set(f"Total Fees Sum: ${total_fees:,.0f}")
        elif structure == "Queue":
            count = len(self.queue_data)
            self.report_var.set(f"Total Records in Queue: {count}")
        elif structure == "List":
            if not self.list_data:
                self.report_var.set("Average Income: $0 (Empty List)")
            else:
                avg_income = sum(item.current_income for item in self.list_data) / len(self.list_data)
                self.report_var.set(f"Average Income: ${avg_income:,.2f}")

    def clear_fields(self):

        self.id_type_var.set("CC")
        self.id_number_var.set("")
        self.full_name_var.set("")
        self.income_var.set("")
        self.employment_var.set("Employee")
        self.service_var.set("Unemployment subsidy")
        self.fee_var.set("0")
        now = datetime.now()
        self.day_var.set(f"{now.day:02d}")
        self.month_var.set(f"{now.month:02d}")
        self.year_var.set(str(now.year))
        self.txt_id_number.focus()

    def refresh_treeview(self):
 
        for row in self.tree.get_children():
            self.tree.delete(row)

        structure = self.structure_var.get()
        self.lbl_tree_title.config(text=f"{structure} — Registered Affiliates")

        if structure == "Stack":
            active_collection = self.stack_data
        elif structure == "Queue":
            active_collection = self.queue_data
        else:
            active_collection = self.list_data

        for affiliate in active_collection:
            self.tree.insert("", "end", values=affiliate.to_tuple())


        self.generate_report()

    def exit_app(self):
        """Requisito 7: Termina la ejecución de la aplicación."""
        self.root.destroy()


# =====================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# =====================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()