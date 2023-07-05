from Producto import Producto
from Cliente import Cliente
from Venta import Venta
from Motorizado import Motorizado
from Desglose import Desglose
from Envio import Envio
from Envio import Delivery
from Pago import Pago 
from Producto import Productocliente
import json
import requests

class Tienda:
    #Listas que serán cambiadas por el programa
    def __init__(self):
      #Lista de productos
        self.productos = []
        
        self.productocliente = []
      #Lista de clientes
        self.clientes = []
      #Lista de ventas
        self.ventas = []
        #temporal
        self.ventas2 = []
      #Lista de Informes
        self.informes = []
      #Lista de envios 
        self.envios = []
      #Lista de pagos
        self.pagos = []
      #Motorizados
        self.motorizados = []


    def get_api(self):
        #print para verificar que se esté llamando al API correctamente
        print(requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json"))

        response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json").text
        
        #Variable para guardar el texto
        objeto = json.loads(response)
        print(objeto)
        for i in objeto:
        #Conversion a objetos del tipo Producto
         nuevo_producto = Productocliente(i["name"], i["description"], i["price"], i["category"])
         self.productocliente.append(nuevo_producto)
         new_product = Producto(i["name"], i["description"], i["price"], i["category"], i["quantity"])
         self.productos.append(new_product)
         
         #Motorizado de prueba(Es para no andarlos registrando)
        moto =[
    {
        "name": "Alex",
        "last_name": "Ferrer",
        "cellphone": "04122345678"

    } 
        ]
        for i in moto:
            
        #Agregar motorizado
            new_motorizado = Motorizado(i["name"], i["last_name"], i["cellphone"])
            self.motorizados.append(new_motorizado)
        #Mostrar motorizados
        for i in range(len(self.motorizados)):
            print(f"{i+1}. {self.motorizados[i].show()}")

    def pause(self):
        #Pausa activa que se usan en casi todos los metodos, así la pantalla se ve más organizada al hacerle run
        print("Toque cualquier botón para volver al menú")
        pause = input(" ")
        if pause == "":
         pass
        else:
         pass
     
    def agregar_producto(self):
        #Se agregan nuevos objetos del tipo producto a la lista self.productos
        qty = (input("Cuántos productos deseas agregar?: "))
        while any(chr.isalpha() for chr in qty) or not qty.isdigit():
            qty = input("Error! Ingrese un numero: ")
        qty = int(qty)
        for i in range(qty):
            name = input("Ingrese el nombre del producto: ")
            name=name.lower()
            name=name.title()
            
            while (not (all(c.isalpha() or c==' ' for c in name))):
                name = input("Error! Dato inválido. Ingrese el nombre del producto: ")
                name=name.lower()
                name=name.title()
                
            description = input("Ingrese la descripción del producto: ")
            
            price = input("Ingrese el precio del producto: ")
            while any(chr.isalpha() for chr in price) or not price.isdigit():
                price = input("Error! Dato inválido. Ingrese el precio del producto: ")
                
            category = input("Ingrese la categoría del producto: ")
            category=category.lower()
            category=category.title()
            while any(chr.isdigit() for chr in category) or not category.isalpha():
                category = input("Error! Escriba una categoria correcta del producto, solo una palabra: ")
                category = category.lower()
                category = category.title()
            
            quantity = input("Ingrese la cantidad del producto: ")
            
            
            while any(chr.isalpha() for chr in quantity) or not quantity.isdigit():
                quantity = input("Error! Dato inválido. Ingrese el stock del producto: ")   
            nuevo_productocliente = Productocliente(name,description,price,category)   
            self.productocliente.append(nuevo_productocliente)
            nuevo_producto = Producto(name,description,price,category,quantity)
            self.productos.append(nuevo_producto)
            
            print(f"Se ha registrado un nuevo producto: {name} ")
                  
    def modify_product(self):
        #Modifica un producto
        name = input("Introduce el nombre del producto a modificar: ")
        name=name.lower()
        name=name.title()
        final = 0
        Existencia = 0
        while final == 0:
            for producto in self.productos:
                    if producto.name == name:
                        Existencia = 1
                        final = final + 1
                        print(f""" Producto {name} encontrado!""")
                        #Lista de opciones del metodo
                        opciones = ["Modificar Nombre", "Modificar Descripción","Modificar Precio","Modificar Categoría", "Modificar Cantidad", "Cancelar"]
                        #Lista de opciones que se usa con el metodo self.menucito
                        self.menucito(opciones)
                        eleccion = input("Ingrese el número de la opcion que desee: ")
                        #Validacion del rango de opciones
                        
                        if eleccion == "1":
                            for prodcliente in self.productocliente:
                                if prodcliente.name == producto.name:
                                    #Validacion de nombre
                                    producto.name = input("Escriba el nuevo nombre del producto: ")
                                    producto.name = producto.name.lower()
                                    producto.name = producto.name.title()
                                    while (not (all(c.isalpha() or c==' ' for c in name))):
                                        producto.name = input("Error! Escriba el nuevo nombre del producto: ")
                                        producto.name = producto.name.lower()
                                        producto.name = producto.name.title()
                                
                                    prodcliente.name = producto.name
                                            
                                            
                                    print(f"""El producto {name} se ha modificado: """)
                                    print(producto.show())
                            
                        elif eleccion == "2":
                            for prodcliente in self.productocliente:
                                if prodcliente.name == producto.name:
                                    producto.description = input("Escriba la nueva descripcion del producto: ")
                                    print(f"""El producto {name} se ha modificado: """)
                                    print(producto.show())
                                    
                                    prodcliente.description = producto.description
                                    
                        elif eleccion == "3":  
                            for prodcliente in self.productocliente:
                                if prodcliente.name == producto.name:
                            #Validacion de precio
                                    producto.price = input("Escriba el nuevo precio del producto: ")
                                    while any(chr.isalpha() for chr in producto.price) or not producto.price.isdigit():
                                        producto.price = input("Error! Ingrese el precio del producto: ")
                                    print(f"""El producto {name} se ha modificado: """)
                                    print(producto.show())
                                    prodcliente.price = producto.price
                            
                        elif eleccion == "4": 
                            for prodcliente in self.productocliente:
                                if prodcliente.name == producto.name:
                                    producto.category = input("Escriba la nueva categoria del producto: ")
                                    producto.category = producto.category.lower()
                                    producto.category = producto.category.title()
                                    while any(chr.isdigit() for chr in producto.category) or not producto.category.isalpha():
                                        producto.category = input("Error! Escriba la nueva categoria del producto, solo una palabra: ")
                                        producto.category = producto.category.lower()
                                        producto.category = producto.category.title()
                                    print(f"""El producto {name} se ha modificado: """)
                                    print(producto.show())
                                    
                                    prodcliente.category = producto.category
                            
                        elif eleccion == "5": 
                            #Validacion de entero
                            producto.quantity = input("Escriba la nueva cantidad del producto: ")
                            while any(chr.isalpha() for chr in producto.quantity) or not producto.quantity.isdigit():
                                producto.quantity = input("Error! Ingrese la cantidad del producto ")
                            print(f"""El producto {name} se ha modificado: """)
                            print(producto.show())
                            
                        elif eleccion == "6": 
                            print("Nada ha cambiado")
                            pass
                    else: 
                        Existencia = 0
                        final = final + 1
        if Existencia == 0:
            #Despues de la creacion devuelve al menu
            print("El producto no fue encontrado")
            choice = input("Te gustaría agregar un nuevo producto? Y/N ")
            choice = self.ver_yn(choice)
            if choice == "Y":
                self.agregar_producto()
            else:
                pass      
    
        #Llamada a la pausa
        self.pause()


    def delete_product(self):
        #Elimina un producto de la lista self.productos
        dele = input("Ingresa el nombre del producto que quieres borrar: ")
        for producto in self.productos:
            if producto.name == dele:
                posicion = self.productos.index(producto)
                choice = input(f"""Se borrará el producto {dele}, continuar? (Y/N): """)
                choice = self.ver_yn(choice)
                if choice == "Y":
                    self.productos.pop(posicion)
                    self.productocliente.pop(posicion)      
                elif choice == "N":
                    print("Cancelado")
          
        #Llamada a la pausa
        self.pause() 
        
    def registrar_pago(self, cliente, total):
        cliente = cliente
        factura = total
        opciones = ["Tarjeta", "Pago móvil","Zelle"]
        self.menucito(opciones)
        eleccion = int(input("Cuál será su método de pago?"))
        metpago = opciones[eleccion]
                    
        opciones = ["MRW", "Zoom","Delivery"]
        self.menucito(opciones)
        eleccion = int(input("Por cuál medio desea el delivery? "))
        metenvio = opciones[eleccion]
                    
        subtotal = 0
        for producto in self.carrito:
             if producto.price > 0:
                subtotal = subtotal + producto.price
                descuento = 0
                iva = subtotal * 0.3
             if metpago == "Zelle" or metpago == "Tarjeta":
                    igtf = subtotal * 0.3
                    divisa = "USD"
             else:
                    igtf = 0
                    divisa = "VEF"
                    
        tipo = metpago
        total = subtotal + igtf + iva
                    
        factura = Desglose(subtotal, descuento, iva, igtf, total)
         

    def registrar_venta(self):
            dni = input("Ingresa el DNI del cliente: ")
            for client in self.clientes:
                if client.dni == dni:
                    cliente = client
                    self.carrito = []
                    aux = 0
                    print("Cliente encontrado con éxito!")
                    choice = input("Deseas agregar mas productos a tu carrito? Y/N ")
                    choice = self.ver_yn(choice)
                    if choice == "Y":

                        while aux == 0:
                            self.mostrar_productos()
                            eleccion = int(input("Seleccione el índice del producto que desea elegir: "))
                            if eleccion not in range(len(self.productos) + 1):
                                print("El indice del producto no existe")
                            for i in range(len(self.productos)):
                                if i+1 == eleccion:
                                    carrito_temp = []
                                    
                                    print(f"{self.productos[i].show()}")
                                    cosa = self.productos[i]
                                    
                                    carrito_temp.append(cosa)
                                    
                                    cosa2 = self.productocliente[i]
                                    
                                    for stock in carrito_temp:
                                        if stock.quantity > 0:
                                            self.carrito.append(cosa2)
                                            stock.quantity = stock.quantity - 1
                                        else:
                                            print("Este producto no tiene existencias")
                                        
                                    
                                    print("Su carrito hasta ahora:")
                                    for j in range(len(self.carrito)):
                                        print(f"{j+1}. {self.carrito[j].show()}")
                                    carrito_temp.clear()
                                    choice = input("Desea agregar otro producto? Y/N ")
                                    choice = self.ver_yn(choice)
                                    if choice == "Y":
                                        pass
                                    elif choice == "N":
                                        aux = aux+1
                            print("Su carrito final es: ")
                            #Muestra el carrito completo
                            for j in range(len(self.carrito)):
                                    print(f"{j+1}. {self.carrito[j].show()}")
                                    
                    if choice == "N":
                        pass
                    if len(self.carrito) > 0:
                        self.factu = []
                        
                        compras = self.carrito
                        opciones = ["Tarjeta", "Pago móvil","Zelle"]
                        self.menucito(opciones)
                        eleccion = (input("Cuál será su método de pago? "))
                        while any(chr.isalpha() for chr in eleccion) or not eleccion.isdigit():
                            eleccion = (input("Cuál será su método de pago? (Ingrese un número) "))
                        eleccion = int(eleccion)
                        metpago = opciones[eleccion-1]
                        
                        opciones = ["MRW", "Zoom","Delivery"]
                        self.menucito(opciones)
                        eleccion = (input("Por cuál medio desea la entrega? "))
                        while any(chr.isalpha() for chr in eleccion) or not eleccion.isdigit():
                            eleccion = (input("Cuál será su método de envio? (Ingrese un número) "))
                            
                        eleccion = int(eleccion)
                        metenvio = opciones[eleccion-1]
                        
                        subtotal = 0
                        
                        for producto in self.carrito:
                            if producto.price > 0:
                                subtotal = subtotal + producto.price
                                
                        iva = subtotal * 0.3
                        if client.tipo == "Juridico":
                            descuento = subtotal * 0.05
                        else: 
                            descuento = 0
                        if metpago == "Zelle" or metpago == "Tarjeta":
                            
                            igtf = subtotal * 0.3
                            divisa = "USD"
                            tipo = metpago
                            
                            
                        else:
                            igtf = 0
                            divisa = "VEF"
                            tipo = metpago
                            
                        if metenvio == "MRW" or metenvio == "Zoom":
                            cliente = cliente
                            orden = compras
                            servicio = metenvio
                            costo = 6
                            fecha = input("Inserte la fecha de hoy: ")
                            while not any(chr.split("/") for chr in fecha):
                                fecha = input("Error! Ingrese una fecha valida con el siguiente formato: DY/MT/YR ")
                            
                            new_envio = Envio(cliente, orden, servicio , costo, fecha)
                            self.envios.append(new_envio)
                            
                            
                        elif metenvio == "Delivery":
                            cliente = cliente
                            orden = compras
                            servicio = metenvio
                            costo = 3
                            motorizado = self.motorizados[-1]
                            fecha = input("Inserte la fecha de hoy: ")
                            while not any(chr.split("/") for chr in fecha):
                                fecha = input("Error! Ingrese una fecha valida con el siguiente formato: DY/MT/YR ")
                            
                            new_envio = Delivery(cliente, orden, servicio , costo, fecha, motorizado)
                            self.envios.append(new_envio)
                            
                        envio = costo
                        total = subtotal + igtf + iva + costo - descuento
                        
                        factura = Desglose(subtotal, descuento, iva, igtf, envio,  total)

                        fecha = fecha
                        
                        new_pago = Pago(cliente,factura,divisa,tipo,fecha)
                        self.pagos.append(new_pago)
                        nueva_venta = Venta(cliente, compras , metpago, metenvio, factura, fecha)
                        self.ventas.append(nueva_venta)
                        self.ventas2.append(nueva_venta)
                        
                        print("A continuacion se imprimirá tu factura")
                        print("envio: ")
                        print(new_envio.show())
                        print("factura")
                        print(nueva_venta.show())
                        
                        for i in range(len(self.ventas2)):
                            pass
                            for j in self.ventas:
                                print("Productos comprados: ")
                            for n in j.compras:
                                print(n.show())
                                print("----------------------------")
                                
                        self.ventas2.clear()
                        
                        #Llamada a la pausa
                        self.pause() 
                    else:
                        print("El carrito esta vacio")
                        pass

                else:
                    print("El cliente no existe")
                    choice = input("Deseas agregar el cliente al sistema? Y/N ")
                    choice = self.ver_yn(choice)
                    if choice == "Y":
                        self.agregar_cliente()
                    elif choice == "N":
                        print("Regresando al menú...")
                        
                        #Llamada a la pausa
                        self.pause() 

    
    def search_pago(self):
        print("Como desea buscar el Pago?")
        opciones = ["Fecha","Tipo de pago", "Moneda de pago"]
        self.menucito(opciones)
        eleccion = input("Ingrese el número de la opción que desee: ")
        
        #Validacion de nombre
        if eleccion == "1":
            fecha = input("Ingresa la fecha del pago que deseas buscar: ")
                
            for pago in self.pagos:
                if pago.fecha == fecha:
                    print("El pago si existe: ")
                    print(pago.show())

        if eleccion == "2":
            tipo = input("Ingresa el tipo del pago que deseas buscar: ")
            for pago in self.pagos:
                if pago.tipo == pago:
                    print("El pago si existe: ")
                    print(pago.show())
                else:
                    pass
        if eleccion == "3":
            divisa = input("Ingresa la divisa del pago que deseas buscar: ")
            for pago in self.pagos:
                if pago.tipo == pago:
                    print("El pago si existe: ")
                    print(pago.show())
                else:
                    pass            
            
                
        if eleccion == "3":
            name = input("Ingresa el nombre del producto que deseas buscar: ")
            name=name.lower()
            name=name.title()
            while any(chr.isdigit() for chr in name) or not name.isalpha():
                name = input("Error! Ingrese un nombre válido: ")
                name=name.lower()
                name=name.title()
                    
            for producto in self.productos:
                if producto.name == name:
                    print("El producto si existe: ")
                    print(producto.show())
                    Existencia = 1
            if Existencia == 0:
                print(f"""El producto {name} no existe""")
                #Despues de la creacion devuelve al menu
                choice = input("Te gustaría agregar un nuevo producto? Y/N ")
                choice = self.ver_yn(choice)
                if choice == "Y":
                    self.agregar_producto()
                else:
                    pass
                
        if eleccion == "4":
            pass
                

        #Llamada a la pausa
        self.pause()
            
    def search_product(self):
        #Variable auxliar para agregar el producto de ser el caso
        Existencia = 0
        print("Como desea buscar el Producto?")
        opciones = ["Categoria", "Precio","Nombre", "Cerrar"]
        self.menucito(opciones)
        eleccion = input("Ingrese el número de la opción que desee: ")
        
        #Validacion de nombre
        if eleccion == "1":
            category = input("Ingresa la categoria del producto que deseas buscar: ")
            category = category.lower()
            category = category.title()
            while any(chr.isdigit() for chr in category) or not category.isalpha():
                category = input("Error! Escriba la categoria del producto, solo una palabra: ")
                category = category.lower()
                category = category.title()
                
            for producto in self.productos:
                if producto.category == category:
                    print("El producto si existe: ")
                    print(producto.show())
                    Existencia = 1
            if Existencia == 0:
                print(f"""El producto no existe""")
                #Despues de la creacion devuelve al menu
                choice = input("Te gustaría agregar un nuevo producto? Y/N ")
                choice = self.ver_yn(choice)
                if choice == "Y":
                    self.agregar_producto()
                else:
                    pass
                
        if eleccion == "2":
            price = input("Ingresa el precio del producto que deseas buscar: ")
            while any(chr.isalpha() for chr in price) or not price.isdigit():
                price = input("Error! Ingrese el precio correctamente: ")
            for producto in self.productos:
                if producto.price == price:
                    print("El producto si existe: ")
                    print(producto.show())
                    Existencia = 1
            if Existencia == 0:
                print(f"""El producto no existe""")
                #Despues de la creacion devuelve al menu
                choice = input("Te gustaría agregar un nuevo producto? Y/N ")
                choice = self.ver_yn(choice)
                if choice == "Y":
                    self.agregar_producto()
                else:
                    pass
                
        if eleccion == "3":
            name = input("Ingresa el nombre del producto que deseas buscar: ")
            name=name.lower()
            name=name.title()
            while any(chr.isdigit() for chr in name) or not name.isalpha():
                name = input("Error! Ingrese un nombre válido: ")
                name=name.lower()
                name=name.title()
                    
            for producto in self.productos:
                if producto.name == name:
                    print("El producto si existe: ")
                    print(producto.show())
                    Existencia = 1
            if Existencia == 0:
                print(f"""El producto {name} no existe""")
                #Despues de la creacion devuelve al menu
                choice = input("Te gustaría agregar un nuevo producto? Y/N ")
                choice = self.ver_yn(choice)
                if choice == "Y":
                    self.agregar_producto()
                else:
                    pass
                
        if eleccion == "4":
            pass
                

        #Llamada a la pausa
        self.pause()
                        
    
    def agregar_cliente(self):
        qty = (input("Cuántos clientes deseas agregar?: "))
        while any(chr.isalpha() for chr in qty) or not qty.isdigit():
            qty = input("Error! Ingrese un numero: ")
        qty = int(qty)
        for i in range(qty):
            #Validacion de nombre
            name=input("Ingrese el nombre del cliente: ")
            name=name.lower()
            name=name.title()
            while any(chr.isdigit() for chr in name) or not name.isalpha():
                name = input("Error! Ingrese el nombre del cliente: ")
                name=name.lower()
                name=name.title()
            
            #Validacion de nombre
            last_name=input("Ingrese el apellido del cliente: ")
            last_name=last_name.lower()
            last_name=last_name.title()
            while any(chr.isdigit() for chr in last_name) or not last_name.isalpha():
                last_name = input("Error! Ingrese el apellido del cliente: ")
                last_name=last_name.lower()
                last_name=last_name.title()
            
            #Validacion de DNI
            dni=input("Ingrese el DNI del cliente: ")
            #Validacion si el DNI existe dentro de la lista de clientes
            dni = self.ver_dni(dni)
                    
            while any(chr.isalpha() for chr in dni) or not dni.isdigit():
                dni = input("Error! Ingrese el DNI del cliente:  ")

                
            #Validacion de email
            email=input("Ingrese el correo electrónico del cliente: ")
            email=email.lower()
            while email.endswith("@") or email.endswith(".") or email.startswith(".") or email.startswith("@") or not any(chr.split("@") for chr in email) or not any(chr=="." for chr in email):
                email = input("Error! Ingrese el correo electrónico del cliente: /Formato de ejemplo = tienda@tienda.com ")
                email=email.lower()
                
            direction = input("Escriba la dirección del cliente: ")
            
            #Validacion de celular
            cellphone=input("Ingrese el número de teléfono del cliente: ")
            while any(chr.isalpha() for chr in cellphone) or not cellphone.isdigit() or not len(cellphone)==11:
                 cellphone = input("Error! Ingrese el número de teléfono del cliente: /Formato de ejemplo = 04XX-1234567, sin guiones ")
                 
            choice = input("Es cliente Juridico? Y/N ")
            choice = self.ver_yn(choice)
            tipo = "Natural"
            if choice == "Y":
                tipo = "Juridico"
            nuevo_cliente = Cliente(name,last_name,dni,email,direction,cellphone,tipo)
            self.clientes.append(nuevo_cliente)
            print(f"Se ha registrado un nuevo cliente: {name} ")
            
            #Llamada a la pausa
            
    def delete_client(self):
        #Cliente borrado se elimina de la lista self.clientes
        dele = input("Ingresa el DNI del cliente que quieres borrar: ")
        for client in self.clientes:
            if client.dni == dele:
                self.mostrar_clientes()
                #Pide el indice del cliente para borrarlo
                posicion = self.clientes.index(client) - 1
                choice = input(f"""Se borrará el cliente {dele}, continuar? (Y/N): """)
                self.ver_yn(choice)
                if choice == "Y":
                    self.clientes.pop(posicion)   
                    #Llamada a la pausa
                    self.pause()    
                elif choice == "N":
                    print("Cancelado")
                    #Llamada a la pausa
                    self.pause() 
                    
                    
                    
    #Verificacion de Si o no como Y y N, las utilizo en metodos de registro y eleccion                
    def ver_yn(self,choice):
        choice = choice.upper()
        elec = 0
        while elec == 0:
            choice = choice.upper()
            if choice == "Y" or choice == "N":
                elec = elec+1
            else:
                choice = input("Seleccion inválida, por favor selecciona Y o N ")
                elec = 0
                
        return choice
                
    def ver_dni(self,dni):
        while any(chr.isalpha() for chr in dni) or not dni.isdigit():
                dni = input("Error! Ingrese el DNI del cliente:  ")
        for client in self.clientes:
                    if client.dni == dni:
                     while client.dni == dni:
                        print("Este DNI ya se registró, por favor ingrese el correcto: ")
                        dni = input("Error! Ingrese el DNI del cliente:  ")
                        while any(chr.isalpha() for chr in dni) or not dni.isdigit():
                             dni = input("Error! Ingrese el DNI del cliente:  ")
            
        return dni
    
    def ver_name(self,name):
        for client in self.clientes:
                    if client.name == name:
                     print("Este dato ya se registró, por favor ingrese el correcto: ")
                     while client.name == name:  
                            name = input("Error! Ingrese el dato correcto:  ")
                            while any(chr.isdigit() for chr in name) or not name.isalpha():
                             name = input("Error! Ingrese el dato correcto:  ")
        
        return name
            
    #Búsqueda de cliente en la lista clientes, si no hay clientes agregados primeros no mostrará nada y se irá al menú
    def search_client(self):
        #Variable auxiliar existencia para decir si un cliente existe o no
        Existencia = 0
        print("Como desea buscar el cliente?")
        opciones = ["DNI", "Email", "Cerrar"]
        self.menucito(opciones)
        eleccion = input("Ingrese el número de la opción que desee: ")
        if eleccion == "1":
            dni = input("Ingresa el DNI del cliente que deseas buscar: ")
            while any(chr.isalpha() for chr in dni) or not dni.isdigit():
                dni = input("Error! Ingrese el DNI del cliente:  ")
            for client in self.clientes:
                if client.dni == dni:
                    print(client.show())
                    Existencia = 1
            if Existencia == 0:
                print(f"""El cliente {dni} no existe""")
                #Despues de la creacion devuelve al menu
                choice = input("Te gustaría agregar un nuevo cliente? Y/N ")
                self.ver_yn(choice)
                if choice == "Y":
                    self.agregar_cliente()
                else:
                    pass
        if eleccion == "2":
            email = input("Ingresa el Email del cliente que deseas buscar: ")
            email=email.lower()
            while email.endswith("@") or email.endswith(".") or email.startswith(".") or email.startswith("@") or not any(chr.split("@") for chr in email) or not any(chr=="." for chr in email):
                email = input("Error! Ingrese el correo electrónico del cliente: /Formato de ejemplo = tienda@tienda.com ")
                email=email.lower()
            for client in self.clientes:
                if client.email == email:
                    print(client.show())
                    Existencia = 1
            if Existencia == 0:
                print(f"""El cliente {dni} no existe""")
                #Despues de la creacion devuelve al menu
                choice = input("Te gustaría agregar un nuevo cliente? Y/N ")
                self.ver_yn(choice)
                if choice == "Y":
                    self.agregar_cliente()
                else:
                    pass
            
            
    def search_ventas(self):
        #Variable auxiliar existencia para decir si un cliente existe o no
        print("Como desea buscar la venta?")
        opciones = ["Cliente", "Fecha", "Monto total"]
        self.menucito(opciones)
        eleccion = input("Ingrese el número de la opción que desee: ")
        
        if eleccion == "1":
            name = input("Ingresa el nombre del cliente")
            for j in self.ventas:
                if j.name == name:
                    print(j.show())
     
        if eleccion == "2":
            fecha = input("Ingresa la fecha del envio que deseas buscar: ")
            for venta in self.ventas:
                if venta.fecha == fecha:
                    print(venta.show())
        if eleccion == "3":
            total = input("Ingresa el monto de la venta")
            for j in self.facturas:
                if j.fecha == total:
                    print(j.show())
             
                    
    def search_envio(self):
        #Variable auxiliar existencia para decir si un cliente existe o no
        print("Como desea buscar el envio?")
        opciones = ["Cliente", "Fecha"]
        self.menucito(opciones)
        eleccion = input("Ingrese el número de la opción que desee: ")
        
        if eleccion == "1":
            name = input("Ingresa el nombre del cliente")
            for j in self.envios:
                if j.name == name:
                    print(j.show())
           
        if eleccion == "2":
            fecha = input("Ingresa la fecha del envio que deseas buscar: ")
            for envio in self.envios:
                if envio.fecha == fecha:
                    print(envio.show())


        
    def modify_client(self):
        dni = input("Introduce el DNI del cliente a modificar: ")
        while any(chr.isalpha() for chr in dni) or not dni.isdigit():
                dni = input("Error! Ingrese el DNI del cliente:  ")
        final = 0
        Existencia = 0
        while final == 0:
            for client in self.clientes:
                if client.dni == dni:
                    Existencia = Existencia + 1
                    final = final + 1
                    
                    print(f""" Cliente {dni} encontrado!""")
                    
                    #Lista de opciones que se usa con el metodo self.menucito
                    opciones = ["Modificar Nombre", "Modificar Apellido","Modificar DNI","Modificar email", "Modificar direccion", "Modificar telefono", "Cerrar"]
                    self.menucito(opciones)
                    eleccion = input("Ingrese el número de la opción que desee: ")
                    
                    if eleccion == "1":
                        client.name = input("Escriba el nuevo nombre del cliente: ")
                        client.name = client.name.lower()
                        client.name = client.name.title()
                        while any(chr.isdigit() for chr in client.name) or not client.name.isalpha():
                            client.name = input("Error! Ingrese el nombre del cliente: ")
                            client.name=client.name.lower()
                            client.name=client.name.title()
                        print(f"""El cliente {dni} se ha modificado: """)
                        print(client.show())
                        
                    elif eleccion == "2":
                        client.last_name = input("Escriba el nuevo apellido del cliente: ")
                        last_name=last_name.lower()
                        last_name=last_name.title()
                        while any(chr.isdigit() for chr in last_name) or not last_name.isalpha():
                            last_name = input("Error! Ingrese el apellido del cliente: ")
                            last_name=last_name.lower()
                            last_name=last_name.title()
                        print(f"""El cliente {dni} se ha modificado: """)
                        print(client.show())
                        
                    elif eleccion == "3":  
                        client.dni = input("Escriba el nuevo precio del cliente: ")
                        while any(chr.isalpha() for chr in dni) or not dni.isdigit():
                            dni = input("Error! Ingrese el DNI del cliente: ")
                        print(f"""El client {dni} se ha modificado: """)
                        print(client.show())
                        
                    elif eleccion == "4": 
                        client.email = input("Escriba la nueva categoría del cliente: ")
                        email=email.lower()
                        while email.endswith("@") or email.endswith(".") or email.startswith(".") or email.startswith("@") or not any(chr.split("@") for chr in email) or not any(chr=="." for chr in email):
                            email = input("Error! Ingrese el correo electrónico del cliente: /Formato de ejemplo = tienda@tienda.com")
                            email=email.lower()
                        print(f"""El cliente {dni} se ha modificado: """)
                        print(client.show())
                        
                    elif eleccion == "5": 
                        client.direction = input("Escriba la nueva cantidad del cliente: ")
                        print(f"""El cliente {dni} se ha modificado: """)
                        print(client.show())
                        
                    elif eleccion == "6": 
                        client.cellphone = input("Escriba el nuevo número de teléfono del cliente: ")
                        while any(chr.isalpha() for chr in cellphone) or not cellphone.isdigit() or not len(cellphone)==11:
                            cellphone = input("Error! Ingrese el número de teléfono del cliente: /Formato de ejemplo = 04XX-1234567, sin guiones ")
                        print(f"""El cliente {dni} se ha modificado: """)
                        print(client.show())
                        
                    elif eleccion == "7":
                        print("Nada ha cambiado")
                        final = final + 1
                        Existencia = Existencia + 1
                    
                        pass
                    else:
                        final = final - 1
                        print("Opción inválida")
                        
                        
        if Existencia == 0:
        #Despues de la creacion devuelve al menu
            print("El Cliente no fue encontrado")
        choice = input("Te gustaría agregar un nuevo CLIENTE? Y/N ")
        self.ver_yn(choice)
        if choice == "Y":
            self.agregar_cliente()
            final = final + 1
        else:
            final = final + 1  
        #Llamada a la pausa
        self.pause()             
        
    def mostrar_ventas(self):
        
        for i in range(len(self.ventas)):
            print(f"{i+1}. {self.ventas[i].show()}") 
            for j in self.ventas:
                print("Productos comprados: ")
                for n in j.compras:
                    print(n.show())
                    print("----------------------------")
                
                
    def mostrar_envios(self):
        print("----------------------------")
        for i in range(len(self.envios)):
            print(f"{i+1}. {self.envios[i].show()}")
            print("----------------------------")        
             
    def mostrar_clientes(self):
        print("----------------------------")
        for i in range(len(self.clientes)):
            print(f"{i+1}. {self.clientes[i].show()}")
            print("----------------------------")
            
    def mostrar_productos(self):
        print("----------------------------")
        for i in range(len(self.productos)):
            print(f"{i+1}. {self.productos[i].show()}")
            print("----------------------------")
            
    def mostrar_productoscliente(self):
        print("----------------------------")
        for i in range(len(self.productocliente)):
            print(f"{i+1}. {self.productocliente[i].show()}")
            print("----------------------------")
            
    def mostrar_pagos(self):
        print("----------------------------")
        for i in range(len(self.pagos)):
            print(f"{i+1}. {self.pagos[i].show()}")
            print("----------------------------")
        
    def menucito(self,opciones):
        print("----------------------------")
        for opcion in range(len(opciones)):
                print(f"{opcion+1} / {opciones[opcion]}")
                print("----------------------------")

    def menu(self):
        Start = 0
        if Start == 0:
            self.get_api()
            Start+1
        #Lista de opciones que se usa con el metodo self.menucito
        opciones = ["Mostrar productos", "Agregar producto", "Buscar producto", "Modificar producto", "Eliminar producto","Registrar cliente" ,"Mostrar clientes", "Buscar cliente","Modificar cliente" ,"Mostrar ventas", "Registrar venta", "Buscar venta", "Mostrar pagos", "Buscar pago","Mostrar envios", "Buscar envio", "Salir"]
        final = 0
        while final == 0:
            print(f"""
                    HOLA! 
                BIENVENIDO A
            "Tiendita Mamá luchona"

                """)
            self.menucito(opciones)

            eleccion = input("Ingrese el número de la opción que desee: ")
            if eleccion == "1":
                self.mostrar_productos()
                self.pause()       
            elif eleccion == "2":
                self.agregar_producto()
                self.pause()  
            elif eleccion == "3":
                self.search_product()
                self.pause()      
            elif eleccion == "4":
                self.modify_product()
            elif eleccion == "5":
                self.delete_product()
            elif eleccion == "6":
                self.agregar_cliente()
                self.pause()  
            elif eleccion == "7":
                self.mostrar_clientes()
                self.pause()      
            elif eleccion == "8":
                self.search_client()
                self.pause()      
            elif eleccion == "9":
                self.modify_client()
            elif eleccion == "10":
                self.mostrar_ventas()
                self.pause()  
            elif eleccion == "11":
                self.registrar_venta()
            elif eleccion == "12":
                self.search_ventas()
                self.pause()      
            elif eleccion == "13":
                self.mostrar_pagos()
                self.pause()  
            elif eleccion == "14":
                self.search_pago()
                self.pause() 
            elif eleccion == "15":
                self.mostrar_envios()
                self.pause()  
            elif eleccion == "16":
                self.search_envio()
                self.pause()
            elif eleccion == "17":
                final = final + 1
                print("Final del programa")
            else:
                print("Error, seleccione un numero valido")
                self.pause()
