D1 = [
    "D1","Mitsubishi Lancer RS",220,(219,300),6200,5.9,1997,4]
H4 = [
    "H4","VW Polo Super 1600", 185,(158,215), 7600,8,1600,4]
D4 = [
    "D4", "Peugeot 206 WRC",225,(221,300),5600,5.4,1996,4]
E4 = [
    "E4", "Austin Metro 6", 240,(265,360), 9800,3.4,3600,6]
H2 = [
    "H2", "Mitsubishi Lancer", 198,(213/290),5500,7.2,1997,4]
D3 = [
    "D3","Seat Toledo Marathon",220,(195,330), 8400,5.2,2100,5]
F3 = [
    "F3","Renault Megane",218,(198,270),8400,5.9,1995,4]
F2 = [
    "F2", "Mitsubishi Galant",180,(216,294),5800,6.3,3395,4]
E1 = [
    "E1","Mitsubishi Carisma GT", 225,(313,290),6000,5.2,1996,4]
A2 = [
    "A2","Ford Focus WRC",224,(221,300),5400,5.5,1995,4]
cars = [D1,H4,D4,E4,H2,D3,F3,F2,E1,A2]
def print_all(c):
    print("-----------------------------------------------------------")
    print(f"|{c[0]}                                                            |")
    print(f"|Car Model: {c[1]}       Max Speed: {c[2]} km/h     |")
    print(f"|RPM at Max Power: {c[4]} rpm  0-100 km/h: {c[5]} seconds |")
    print(f"|Engine Capacity: {c[6]} cc    Number of Cylinders: {c[7]}|")
    print("|-----------------------------------------------------------")
i = 1
for car in cars:
    print(car[1])
    i += 1
print("-----------------------------------------------------------")
choice = int(input("Choose a car number: "))
print_all(cars[choice - 1])
