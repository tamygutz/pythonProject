print("Esta es una calculadora de propina")
bill = float(input("Por favor introduce el total de tu cuenta: "))
people = int(input("¿Cuántas personas son?"))

tip_percent = float(12/100)
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_person = total_bill / people
total_total_bill = round(bill_per_person)

print(f"Cada persona debe de pagar: ${total_total_bill}")

