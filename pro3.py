import tkinter as tk
from tkinter import messagebox, simpledialog 
import json 

# Rutas de los archivos para usuarios y cursos
usuarios_file = "usuarios.json"
cursos_file = "cursos.json"
profesores_file = "profesores.json"
cursos_profesores_file = "cursos_profesores.json"
grades_file = "grades.json"
usuarios=()

# Función para cargar datos de prueba desde archivos (simulando la base de datos)
def cargar_datos_prueba():
    global usuarios, cursos, profesores, cursos_profesores, grades
    try:
        with open(usuarios_file, "r") as file:
            usuarios = json.load(file)
    except FileNotFoundError:
        usuarios = []

    try:
        with open(cursos_file, "r") as file:
            cursos = json.load(file)
    except FileNotFoundError:
        cursos = []

    try:
        with open(profesores_file, "r") as file:
            profesores = json.load(file)
    except FileNotFoundError:
        profesores = []

    try:
        with open(cursos_profesores_file, "r") as file:
            cursos_profesores = json.load(file)
    except FileNotFoundError:
        cursos_profesores = []

    try:
        with open(grades_file, "r") as file:
            grades = json.load(file)
    except FileNotFoundError:
        grades = []

# Función para guardar datos en archivos
def guardar_datos():
    with open(usuarios_file, "w") as file:
        json.dump(usuarios, file)

    with open(cursos_file, "w") as file:
        json.dump(cursos, file)

    with open(profesores_file, "w") as file:
        json.dump(profesores, file)

    with open(cursos_profesores_file, "w") as file:
        json.dump(cursos_profesores, file)

    with open(grades_file, "w") as file:
        json.dump(grades, file)



# Función para mostrar el panel de administrador
def mostrar_panel_administrador():
    ventana_administrador = tk.Toplevel(root)
    ventana_administrador.title("Panel de Administrador")
    ventana_administrador.geometry("400x400")

    label = tk.Label(ventana_administrador, text="Bienvenido al panel de administrador.")
    label.pack(pady=10)

    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(ventana_administrador, text="Cerrar", command=ventana_administrador.destroy)
    btn_cerrar.pack(pady=10)

    # Botón para mostrar la lista de cursos
    btn_ver_cursos = tk.Button(ventana_administrador, text="Ver Cursos", command=ver_listado_cursos)
    btn_ver_cursos.pack(pady=10)

    # Botón para agregar un nuevo curso
    btn_agregar_curso = tk.Button(ventana_administrador, text="Agregar Curso", command=agregar_curso)
    btn_agregar_curso.pack(pady=10)

    # Botón para borrar un curso existente
    btn_borrar_curso = tk.Button(ventana_administrador, text="Borrar Curso", command=borrar_curso)
    btn_borrar_curso.pack(pady=10)

    # Botón para asignar cursos a profesores
    btn_asignar_cursos = tk.Button(ventana_administrador, text="Asignar Cursos a Profesores", command=asignar_cursos)
    btn_asignar_cursos.pack(pady=10)

    # Botón para ver el listado de profesores
    btn_ver_profesores = tk.Button(ventana_administrador, text="Ver Profesores", command=ver_listado_profesores)
    btn_ver_profesores.pack(pady=10)

    # Botón para ver los listados de notas de cada curso
    btn_ver_notas = tk.Button(ventana_administrador, text="Ver Listados de Notas", command=ver_listados_notas)
    btn_ver_notas.pack(pady=10)

    # Botón para desbloquear cuentas de usuarios
    btn_desbloquear_cuentas = tk.Button(ventana_administrador, text="Desbloquear Cuentas de Usuarios", command=desbloquear_cuentas)
    btn_desbloquear_cuentas.pack(pady=10)
    
    # Botón para quitar cursos de profesores
    btn_quitar_curso = tk.Button(ventana_administrador, text="Quitar Cursos de Profesores", command=quitar_cursos_profesor)
    btn_quitar_curso.pack(pady=10)

    ventana_administrador.mainloop()
    
# Función para quitar cursos de profesores
def quitar_cursos_profesor():
    # Código para quitar cursos de profesores
    pass
    
def ver_listados_notas():
    ventana_notas = tk.Toplevel(root)
    ventana_notas.title("Listado de Notas")
    ventana_notas.geometry("400x400")

# Función para desbloquear cuentas de usuarios
def desbloquear_cuentas(usuario):
    for usuario in usuarios:
        if usuario["intentos_fallidos"] > 3:
            usuario["bloqueado"] = False
            usuario["intentos_fallidos"] = 0
    guardar_datos()

# Función para ver el listado de profesores
def ver_listado_profesores():
    for profesor in profesores:
        print(profesor)

# Función para ver los listados de notas de cada curso
def ver_listados_notas(curso_id):
    for grade in grades:
        if grade["curso_id"] == curso_id:
            print(grade)

# Función para ver el listado de cursos
def ver_listado_cursos():
    for curso in cursos:
        print(curso)

# Función para agregar un nuevo curso
def agregar_curso(curso):
    cursos.append(curso)
    guardar_datos()

# Función para borrar un curso existente
def borrar_curso(curso_id):
    for curso in cursos:
        if curso["curso_id"] == curso_id:
            cursos.remove(curso)
    guardar_datos()

# Función para asignar cursos a profesores
def asignar_cursos(profesor_id, cursos_asignados):
    cursos_profesores[profesor_id] = cursos_asignados
    guardar_datos()

# Función para crear un nuevo profesor en el panel de administración
def crear_profesor_admin():
    ventana_profesor = tk.Toplevel(root)
    ventana_profesor.title("Crear Nuevo Profesor")
    ventana_profesor.geometry("300x400")

    label_nombre_profesor = tk.Label(ventana_profesor, text="Nombre del Profesor:")
    label_nombre_profesor.grid(row=0, column=0, padx=10, pady=5)
    entry_nombre_profesor = tk.Entry(ventana_profesor)
    entry_nombre_profesor.grid(row=0, column=1, padx=10, pady=5)

    label_apellido_profesor = tk.Label(ventana_profesor, text="Apellido del Profesor:")
    label_apellido_profesor.grid(row=1, column=0, padx=10, pady=5)
    entry_apellido_profesor = tk.Entry(ventana_profesor)
    entry_apellido_profesor.grid(row=1, column=1, padx=10, pady=5)

    label_contrasena_profesor = tk.Label(ventana_profesor, text="Contraseña del Profesor:")
    label_contrasena_profesor.grid(row=2, column=0, padx=10, pady=5)
    entry_contrasena_profesor = tk.Entry(ventana_profesor, show="*")
    entry_contrasena_profesor.grid(row=2, column=1, padx=10, pady=5)

    def guardar_profesor_admin():
        nombre_profesor = entry_nombre_profesor.get()
        apellido_profesor = entry_apellido_profesor.get()
        contrasena_profesor = entry_contrasena_profesor.get()

        if not contrasena_profesor:
            messagebox.showerror("Error", "Ingresa una contraseña para el profesor.")
            return

        nuevo_profesor = {
            "nombre": nombre_profesor,
            "apellido": apellido_profesor,
            "tipo": "profesor",
            "contraseña": contrasena_profesor,
        }

      
        messagebox.showinfo("Profesor Creado", "El profesor ha sido creado exitosamente.")
        ventana_profesor.destroy()

    btn_guardar_profesor = tk.Button(ventana_profesor, text="Guardar Profesor", command=guardar_profesor_admin)
    btn_guardar_profesor.grid(row=8, column=0, columnspan=2, pady=10)

    ventana_profesor.mainloop()

def iniciar_sesion():
    nombre_usuario = entry_username.get()
    contraseña = entry_password.get()
    for user in usuarios:
        if user["nombre_usuario"] == nombre_usuario and user.get("contraseña") == contraseña:
            messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {user['nombre']} {user['apellido']}. Tipo: {user['tipo']}")
            if user['tipo'] == 'administrador':
                mostrar_panel_administrador()
            elif user['tipo'] == 'profesor':
                # Agregar funcionalidad para iniciar sesión como profesor
                iniciar_sesion_profesor(user)
            return
    messagebox.showerror("Error de inicio de sesión", "Nombre de usuario o contraseña incorrectos.")

# Nueva función para iniciar sesión como profesor
def iniciar_sesion():
    nombre_usuario = entry_username.get()
    contraseña = entry_password.get()
    for user in usuarios:
        if user["nombre_usuario"] == nombre_usuario and user.get("contraseña") == contraseña:
            messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {user['nombre']} {user['apellido']}. Tipo: {user['tipo']}")
            if user['tipo'] == 'profesor':
                mostrar_panel_administrador()
            elif user['tipo'] == 'profesor':
                # Agregar funcionalidad para iniciar sesión como profesor
                iniciar_sesion_profesor(user)
            return
    messagebox.showerror("Error de inicio de sesión", "Nombre de usuario o contraseña incorrectos.")

#mostrar ventana de profesor
def iniciar_sesion_profesor(usuario):
    ventana_vprofesor = tk.Toplevel(root)
    ventana_vprofesor.title("Panel de Profesor")
    ventana_vprofesor.geometry("400x400")

    label = tk.Label(ventana_vprofesor, text=f"Bienvenido, {usuario['nombre']} {usuario['apellido']}.")
    label.pack(pady=10)

    # Botón para ver cursos
    btn_cursos = tk.Button(ventana_vprofesor, text="Cursos", command=ver_cursos)
    btn_cursos.pack(pady=10)

    # Botón para ver notas
    btn_notas = tk.Button(ventana_vprofesor, text="Notas", command=ver_notas)
    btn_notas.pack(pady=10)

    # Botón para cerrar sesión
    btn_cerrar_sesion = tk.Button(ventana_vprofesor, text="Cerrar Sesión", command=ventana_vprofesor.destroy)
    btn_cerrar_sesion.pack(pady=10)

    ventana_vprofesor.mainloop()



# Función para crear un nuevo curso (en el panel de administrador)
def crear_curso_admin():
    ventana_crear_curso = tk.Toplevel(root)
    ventana_crear_curso.title("Crear Nuevo Curso")
    ventana_crear_curso.geometry("300x300")

    label_nombre_curso = tk.Label(ventana_crear_curso, text="Nombre del Curso:")
    label_nombre_curso.grid(row=0, column=0, padx=10, pady=5)
    entry_nombre_curso = tk.Entry(ventana_crear_curso)
    entry_nombre_curso.grid(row=0, column=1, padx=10, pady=5)

    label_codigo_curso = tk.Label(ventana_crear_curso, text="Código del Curso:")
    label_codigo_curso.grid(row=1, column=0, padx=10, pady=5)
    entry_codigo_curso = tk.Entry(ventana_crear_curso)
    entry_codigo_curso.grid(row=1, column=1, padx=10, pady=5)

    label_costo_curso = tk.Label(ventana_crear_curso, text="Costo del Curso:")
    label_costo_curso.grid(row=2, column=0, padx=10, pady=5)
    entry_costo_curso = tk.Entry(ventana_crear_curso)
    entry_costo_curso.grid(row=2, column=1, padx=10, pady=5)

    label_horario_curso = tk.Label(ventana_crear_curso, text="Horario del Curso:")
    label_horario_curso.grid(row=3, column=0, padx=10, pady=5)
    entry_horario_curso = tk.Entry(ventana_crear_curso)
    entry_horario_curso.grid(row=3, column=1, padx=10, pady=5)

    label_profesor_curso = tk.Label(ventana_crear_curso, text="Profesor del Curso:")
    label_profesor_curso.grid(row=4, column=0, padx=10, pady=5)
    entry_profesor_curso = tk.Entry(ventana_crear_curso)
    entry_profesor_curso.grid(row=4, column=1, padx=10, pady=5)
    
    # Etiquetas y campos para el profesor del curso
    label_profesor_curso = tk.Label(ventana_crear_curso, text="Profesor del Curso:")
    label_profesor_curso.grid(row=5, column=0, padx=10, pady=5)
    entry_profesor_curso = tk.Entry(ventana_crear_curso)
    entry_profesor_curso.grid(row=5, column=1, padx=10, pady=5)
        
    def guardar_curso_admin():
        nombre_curso = entry_nombre_curso.get()
        codigo_curso = entry_codigo_curso.get()
        costo_curso = entry_costo_curso.get()
        horario_curso = entry_horario_curso.get()
        profesor_curso = entry_profesor_curso.get()

        if not nombre_curso or not codigo_curso or not costo_curso or not horario_curso or not profesor_curso:
            messagebox.showerror("Error", "Completa todos los campos.")
            return

        nuevo_curso = {
            "nombre_curso": nombre_curso,
            "codigo_curso": codigo_curso,
            "costo": costo_curso,
            "horario": horario_curso,
            "profesor": profesor_curso
        }

        cursos.append(nuevo_curso)
        guardar_datos()
        messagebox.showinfo("Curso Creado", "El curso ha sido creado exitosamente.")
        ventana_crear_curso.destroy()

    btn_guardar_curso = tk.Button(ventana_crear_curso, text="Guardar Curso", command=guardar_curso_admin)
    btn_guardar_curso.grid(row=5, column=0, columnspan=2, pady=10)

# Función para eliminar un curso (en el panel de administrador)
def eliminar_curso_admin():
    selected_course = listbox_courses.curselection()

    if not selected_course:
        messagebox.showwarning("Error", "Selecciona un curso para eliminar.")
        return

    index = int(selected_course[0])
    curso_seleccionado = listbox_courses.get(index)
    encontrado = False

    for curso in cursos:
        if curso["nombre_curso"] == curso_seleccionado:
            cursos.pop(index)
            guardar_datos()
            messagebox.showinfo("Curso Eliminado", f"El curso {curso_seleccionado} ha sido eliminado exitosamente.")
            encontrado = True
            break

    if not encontrado:
        messagebox.showerror("Error",f"No se encontró el curso {curso_seleccionado}.")
        
def mostrar_ventana_eliminar_curso():
    # Crear una nueva ventana para mostrar la lista de cursos
    ventana_eliminar_curso = tk.Toplevel(root)
    ventana_eliminar_curso.title("Eliminar Curso")
    ventana_eliminar_curso.geometry("300x200")

    label_cursos = tk.Label(ventana_eliminar_curso, text="Lista de Cursos:")
    label_cursos.pack(pady=10)
    
# Crear un widget Listbox para mostrar la lista de cursos
    listbox_cursos = tk.Listbox(ventana_eliminar_curso, selectmode=tk.SINGLE)
    listbox_cursos.pack(padx=10, pady=10)

    # Insertar los nombres de los cursos en el Listbox
    for curso in cursos:
        listbox_cursos.insert(tk.END, curso["nombre_curso"])

    def eliminar_curso_seleccionado():
        selected_index = listbox_cursos.curselection()

        if not selected_index:
            messagebox.showwarning("Error", "Selecciona un curso para eliminar.")
            return

        index = int(selected_index[0])
        curso_seleccionado = listbox_cursos.get(index)
        encontrado = False

        for curso in cursos:
            if curso["nombre_curso"] == curso_seleccionado:
                cursos.pop(cursos.index(curso))
                guardar_datos()
                messagebox.showinfo("Curso Eliminado", f"El curso {curso_seleccionado} ha sido eliminado exitosamente.")
                encontrado = True
                break

        if not encontrado:
            messagebox.showerror("Error", f"No se encontró el curso {curso_seleccionado}.")

        # Actualizar la lista de cursos
        listbox_cursos.delete(0, tk.END)
        for curso in cursos:
            listbox_cursos.insert(tk.END, curso["nombre_curso"])

    btn_eliminar_curso = tk.Button(ventana_eliminar_curso, text="Eliminar Curso Seleccionado", command=eliminar_curso_seleccionado)
    btn_eliminar_curso.pack(pady=10)

      
#función para mostrar la lista de cursos
def ver_listado_cursos():
    # Crear una nueva ventana para mostrar la lista de cursos
    ventana_cursos = tk.Toplevel(root)
    ventana_cursos.title("Listado de Cursos")
    ventana_cursos.geometry("400x300")

    label_cursos = tk.Label(ventana_cursos, text="Lista de Cursos:")
    label_cursos.pack(pady=10)

    # Crear un widget Listbox para mostrar la lista de cursos
    listbox_cursos = tk.Listbox(ventana_cursos)
    listbox_cursos.pack(padx=10, pady=10)

    # Insertar los nombres de los cursos en el Listbox
    for curso in cursos:
        listbox_cursos.insert(tk.END, curso["nombre_curso"])

    ventana_cursos.mainloop()


#función para mostrar el panel de administrador
def mostrar_panel_administrador():
    ventana_administrador = tk.Toplevel(root)
    ventana_administrador.title("Panel de Administrador")
    ventana_administrador.geometry("400x400")

    label = tk.Label(ventana_administrador, text="Bienvenido al panel de administrador.")
    label.pack(pady=10)

    btn_crear_curso = tk.Button(ventana_administrador, text="Crear Curso", command=crear_curso_admin)
    btn_crear_curso.pack(pady=10)
    
    btn_crear_profesor = tk.Button(ventana_administrador, text="Crear Profesor", command=crear_profesor_admin)
    btn_crear_profesor.pack(pady=10)

    btn_eliminar_curso = tk.Button(ventana_administrador, text="Eliminar Curso", command=mostrar_ventana_eliminar_curso)
    btn_eliminar_curso.pack(pady=10)

    # Agregar un botón para mostrar la lista de cursos
    btn_ver_cursos = tk.Button(ventana_administrador, text="Ver Cursos", command=ver_listado_cursos)
    btn_ver_cursos.pack(pady=10)

    btn = tk.Button(ventana_administrador, text="Cerrar", command=ventana_administrador.destroy)
    btn.pack(pady=10)

    ventana_administrador.mainloop()


# Función para iniciar sesión
def iniciar_sesion():
    nombre_usuario = entry_username.get()
    contraseña = entry_password.get()

    for user in usuarios:
        if 'nombre_usuario' in user and user["nombre_usuario"] == nombre_usuario and user.get("contraseña") == contraseña:
            messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {user['nombre']} {user['apellido']}. Tipo: {user['tipo']}")
            if user['tipo'] == 'administrador':
                mostrar_panel_administrador()
            return

    messagebox.showerror("Error de inicio de sesión", "Nombre de usuario o contraseña incorrectos.")


# Función para crear un nuevo usuario
def crear_usuario():
    def mi_funcion(argumento1, argumento2):
        if argumento1 == 0:
            return argumento2
        else:
            return argumento1

    tipo_usuario = var_tipo_usuario.get()
    nombre = entry_new_name.get()
    apellido = entry_new_lastname.get()
    contraseña = entry_new_password.get()  # Obtener la contraseña ingresada
    dpi = entry_dpi.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    telefono = entry_telefono.get()
    nombre_usuario = entry_nombre_usuario.get()
    
    if not all([tipo_usuario, nombre, apellido, contraseña, dpi, fecha_nacimiento, telefono, nombre_usuario]):
        messagebox.showerror("Error de registro", "Todos los campos son obligatorios. Por favor, completa todos los campos.")

    messagebox.showinfo("Registro exitoso", "El usuario ha sido creado exitosamente.")
    
    # Verificar que el nombre de usuario sea único
for user in usuarios:
    if 'nombre_usuario' in user and user["nombre_usuario"] == nombre_usuario:
        messagebox.showerror("Error de registro", "El nombre de usuario ya está en uso. Por favor, elige otro nombre de usuario.")
        

    nuevo_usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "tipo": "administrador" if tipo_usuario == 2 else ("estudiante" if tipo_usuario == 0 else "profesor"),
        "contraseña": contraseña,
        "dpi": dpi,
        "fecha_nacimiento": fecha_nacimiento,
        "telefono": telefono,
        "nombre_usuario": nombre_usuario
    }

    usuarios.append(nuevo_usuario)
    guardar_datos()
    messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente.")


# Función para asignar cursos a estudiantes
def asignar_cursos():
    global cursos
    selected_courses = listbox_courses.curselection()

    if not selected_courses:
        messagebox.showwarning("Error", "Selecciona al menos un curso.")
        return

    usuario = entry_username.get()

    for index in selected_courses:
        curso = cursos[int(index)]
        if curso["cupo"] > 0:
            curso["cupo"] -= 1
            messagebox.showinfo("Asignación de curso", f"Curso asignado: {curso['nombre_curso']} para el usuario {usuario}.")
        else:
            messagebox.showerror("Error", f"No hay cupo disponible para el curso {curso['nombre_curso']}.")

    guardar_datos()

# Función para mostrar la página de inicio de sesión
def mostrar_pagina_inicio_sesion():
    # Ocultar widgets de registro y asignación de cursos
    frame_register.pack_forget()
    frame_assign_courses.pack_forget()

    # Mostrar widgets de inicio de sesión
    frame_login.pack()

# Función para mostrar la página de registro
def mostrar_pagina_registro():
    # Ocultar widgets de inicio de sesión y asignación de cursos
    frame_login.pack_forget()
    frame_assign_courses.pack_forget()

    # Mostrar widgets de registro
    frame_register.pack()

# Función para mostrar la página de asignación de cursos
def mostrar_pagina_asignar_cursos():
    # Ocultar widgets de inicio de sesión y registro
    frame_login.pack_forget()
    frame_register.pack_forget()

    # Mostrar widgets de asignación de cursos
    frame_assign_courses.pack()
    listbox_courses.delete(0, tk.END)

    for curso in cursos:
        listbox_courses.insert(tk.END, curso["nombre_curso"])

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Gestión Académica")
root.geometry("400x400")  # Ajustado para mostrar todos los widgets

# Cargar datos de prueba
cargar_datos_prueba()

# Crear widgets para el inicio de sesión
frame_login = tk.Frame(root)
frame_login.pack(pady=20)

label_username = tk.Label(frame_login, text="Nombre de usuario:")
label_username.grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(frame_login)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(frame_login, text="Contraseña:")
label_password.grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(frame_login, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

btn_login = tk.Button(frame_login, text="Iniciar Sesión", command=iniciar_sesion)
btn_login.grid(row=2, column=0, columnspan=2, pady=10)

# Crear widgets para el registro de nuevos usuarios
frame_register = tk.Frame(root)

label_new_name = tk.Label(frame_register, text="Nombre:")
label_new_name.grid(row=0, column=0, padx=10, pady=5)
entry_new_name = tk.Entry(frame_register)
entry_new_name.grid(row=0, column=1, padx=10, pady=5)

label_new_lastname = tk.Label(frame_register, text="Apellido:")
label_new_lastname.grid(row=1, column=0, padx=10, pady=5)
entry_new_lastname = tk.Entry(frame_register)
entry_new_lastname.grid(row=1, column=1, padx=10, pady=5)

label_new_password = tk.Label(frame_register, text="Contraseña:")
label_new_password.grid(row=2, column=0, padx=10, pady=5)
entry_new_password = tk.Entry(frame_register, show="*")
entry_new_password.grid(row=2, column=1, padx=10, pady=5)

label_dpi = tk.Label(frame_register, text="DPI:")
label_dpi.grid(row=3, column=0, padx=10, pady=5)
entry_dpi = tk.Entry(frame_register)
entry_dpi.grid(row=3, column=1, padx=10, pady=5)

label_fecha_nacimiento = tk.Label(frame_register, text="Fecha de Nacimiento:")
label_fecha_nacimiento.grid(row=4, column=0, padx=10, pady=5)
entry_fecha_nacimiento = tk.Entry(frame_register)
entry_fecha_nacimiento.grid(row=4, column=1, padx=10, pady=5)

label_telefono = tk.Label(frame_register, text="Teléfono:")
label_telefono.grid(row=5, column=0, padx=10, pady=5)
entry_telefono = tk.Entry(frame_register)
entry_telefono.grid(row=5, column=1, padx=10, pady=5)

label_nombre_usuario = tk.Label(frame_register, text="Nombre de Usuario:")
label_nombre_usuario.grid(row=6, column=0, padx=10, pady=5)
entry_nombre_usuario = tk.Entry(frame_register)
entry_nombre_usuario.grid(row=6, column=1, padx=10, pady=5)

label_tipo_usuario = tk.Label(frame_register, text="Tipo de Usuario:")
label_tipo_usuario.grid(row=7, column=0, padx=10, pady=5)
var_tipo_usuario = tk.IntVar()
var_tipo_usuario.set(0)  # Valor predeterminado: Estudiante
radio_student = tk.Radiobutton(frame_register, text="Estudiante", variable=var_tipo_usuario, value=0)
radio_student.grid(row=7, column=1, padx=10, pady=5)
radio_professor = tk.Radiobutton(frame_register, text="Profesor", variable=var_tipo_usuario, value=1)
radio_professor.grid(row=7, column=2, padx=10, pady=5)
radio_admin = tk.Radiobutton(frame_register, text="Administrador", variable=var_tipo_usuario, value=2)
radio_admin.grid(row=7, column=3, padx=10, pady=5)

btn_create_user = tk.Button(frame_register, text="Crear Usuario", command=crear_usuario)
btn_create_user.grid(row=8, column=0, columnspan=4, pady=10)

# Crear widgets para la asignación de cursos
frame_assign_courses = tk.Frame(root)

label_courses = tk.Label(frame_assign_courses, text="Cursos disponibles:")
label_courses.grid(row=0, column=0, padx=10, pady=5)

listbox_courses = tk.Listbox(frame_assign_courses, selectmode=tk.MULTIPLE)
listbox_courses.grid(row=1, column=0, padx=10, pady=5)

btn_assign_courses = tk.Button(frame_assign_courses, text="Asignar Cursos", command=asignar_cursos)
btn_assign_courses.grid(row=2, column=0, pady=10)

# Mostrar página de inicio de sesión por defecto
mostrar_pagina_inicio_sesion()

# Botones para cambiar entre páginas
btn_to_register = tk.Button(root, text="Registrarse", command=mostrar_pagina_registro)
btn_to_register.pack(pady=5)
btn_to_login = tk.Button(root, text="Iniciar Sesión", command=mostrar_pagina_inicio_sesion)
btn_to_login.pack(pady=5)

# Mostrar la interfaz gráfica
root.mainloop()
