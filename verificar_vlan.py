# Solicitar al usuario que ingrese el número de VLAN
vlan = int(input("Ingrese el número de VLAN: "))

# Determinar si la VLAN es de rango normal o extendido
if 1 <= vlan <= 1005:
    print(f"La VLAN {vlan} corresponde a un rango normal.")
elif 1006 <= vlan <= 4094:
    print(f"La VLAN {vlan} corresponde a un rango extendido.")
else:
    print(f"La VLAN {vlan} no es válida.")
