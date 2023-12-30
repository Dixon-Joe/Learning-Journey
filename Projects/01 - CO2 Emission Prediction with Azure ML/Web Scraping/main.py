import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active
sheet["A1"] = "Price"
sheet["B1"] = "New_Price_Roadworthy"
sheet["C1"] = "Road_Tax_3_Months"
sheet["D1"] = "Body_Type"
sheet["E1"] = "Transmission"
sheet["F1"] = "Number_of_Seats"
sheet["G1"] = "Segment"
sheet["H1"] = "Introduction"
sheet["I1"] = "End"
sheet["J1"] = "Drive_Wheel"
sheet["K1"] = "Engine_motor_Type"
sheet["L1"] = "Fuel_Type"
sheet["M1"] = "Power"
sheet["N1"] = "Total_Max_Power_kW"
sheet["O1"] = "Total_Max_Power_hp"
sheet["P1"] = "Max_Torque"
sheet["Q1"] = "Cylinders"
sheet["R1"] = "Valves_Per_Cylinder"
sheet["S1"] = "Engine_Capacity"
sheet["T1"] = "Bore_X_Stroke"
sheet["U1"] = "Compression_Ratio"
sheet["V1"] = "Max_Power"
sheet["W1"] = "Power_kW"
sheet["X1"] = "Power_hp"
sheet["Y1"] = "Max_Power_Rpm"
sheet["Z1"] = "Max_Torque"
sheet["AA1"] = "Max_Torque_Rpm"
sheet["AB1"] = "Fuel_System"
sheet["AC1"] = "Valve_Actuation"
sheet["AD1"] = "Turbo"
sheet["AE1"] = "Catalyst"
sheet["AF1"] = "Fuel_Tank_Capacity"
sheet["AG1"] = "Top_Speed"
sheet["AH1"] = "Acceleration_0_100_Km_H"
sheet["AI1"] = "Practice_Consumption_Monitor"
sheet["AJ1"] = "Urban_Consumption"
sheet["AK1"] = "Extra_Urban_Consumption"
sheet["AL1"] = "Combined_Consumption"
sheet["AM1"] = "Co2_Emissions"
sheet["AN1"] = "Energy_Label"
sheet["AO1"] = "Power_Consumption"
sheet["AP1"] = "Battery_Range"
sheet["AQ1"] = "Low_Consumption"
sheet["AR1"] = "Medium_Consumption"
sheet["AS1"] = "High_Consumption"
sheet["AT1"] = "Very_High_Consumption"
sheet["AU1"] = "Combined_Consumption"
sheet["AV1"] = "Co2_Emissions"
sheet["AW1"] = "Battery_Range"
sheet["AX1"] = "Power_Consumption"
sheet["AY1"] = "Front_Suspension_1"
sheet["AZ1"] = "Rear_Suspension_1"
sheet["BA1"] = "Front_Suspension_2"
sheet["BB1"] = "Rear_Suspension_2"
sheet["BC1"] = "Front_Stabilizer"
sheet["BD1"] = "Rear_Stabilizer"
sheet["BE1"] = "Front_Brakes"
sheet["BF1"] = "Rear_Brakes"
sheet["BG1"] = "Front_Tire_Size"
sheet["BH1"] = "Rear_Tire_Size"
sheet["BI1"] = "Turning_Circle"
sheet["BJ1"] = "First_Gear"
sheet["BK1"] = "Second_Gear"
sheet["BL1"] = "Third_Gear"
sheet["BM1"] = "Fourth_Gear"
sheet["BN1"] = "Fifth_Gear"
sheet["BO1"] = "Sixth_Gear"
sheet["BP1"] = "Seventh_Gear"
sheet["BQ1"] = "Eighth_Gear"
sheet["BR1"] = "Ninth_Gear"
sheet["BS1"] = "Reverse_Gear"
sheet["BT1"] = "Final_Drive"
sheet["BU1"] = "Rpm_At_120_Km_h"


Column_List = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "AA","AB","AC","AD","AE","AF","AG","AH","AI","AJ","AK","AL","AM","AN","AO","AP","AQ","AR","AS","AT","AU","AV","AW","AX","AY","AZ",
            "BA","BB","BC","BD","BE","BF","BG","BH","BI","BJ","BK","BL","BM","BN","BO","BP","BQ","BR","BS","BT","BU"]
Column = 0    
Row = 2
Wbn = 1
for page in range(1,98):
    print(f"Page {page} Processing")
    driver = webdriver.Chrome()
    web_page = "###"
    driver.get(web_page)
    time.sleep(5)
    
    try:
        href_values = driver.find_elements(by =By.XPATH, value = '//div[@class="col-4"]/a')
        print(f"Page {page} href_values found.")

    except:
        print(f"Page {page} href links not found.")
        pass
    
    href_list = []
    for href_value in href_values:
        try:
            href = href_value.get_attribute("href")
            href_list.append(href)
        except:
            print(f"href link {href} of page {page} not found.")
            pass
        
    driver.quit()
    print(f"Car Links(href_list) appended.")
    time.sleep(5)

    for car_link in href_list:
        if car_link not in ["###","###","###"]:
            driver = webdriver.Chrome()
            web_page = car_link
            web_page += "###" 
            try:
                driver.get(web_page)
                time.sleep(5)
            except:
                pass

            #General
            try:
                Price = driver.find_elements(by =By.XPATH, value = "//td[text()='Price:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Price
                Column += 1
            except:
                Price = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Price
                Column += 1
            try:   
                New_Price_Roadworthy =  driver.find_elements(by =By.XPATH, value = "//td[text()='New Price Roadworthy:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = New_Price_Roadworthy
                Column += 1
            except:
                New_Price_Roadworthy = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = New_Price_Roadworthy
                Column += 1

            try:
                Road_Tax_3_Months =  driver.find_elements(by =By.XPATH, value = "//td[text()='Road Tax / 3 Months:']/following-sibling::td")[0].text 
                sheet[f"{Column_List[Column]}{str(Row)}"] = Road_Tax_3_Months
                Column += 1
            except:
                Road_Tax_3_Months = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Road_Tax_3_Months
                Column += 1  
            try:
                Body_Type =  driver.find_elements(by =By.XPATH, value = "//td[text()='Body Type:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Body_Type
                Column += 1
            except:
                Body_Type = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Body_Type
                Column += 1

            try:
                Transmission =  driver.find_elements(by =By.XPATH, value = "//td[text()='Transmission:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Transmission
                Column += 1
            except:
                Transmission = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Transmission
                Column += 1
            try:
                Number_of_Seats =  driver.find_elements(by =By.XPATH, value = "//td[text()='Number Of Seats:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Number_of_Seats
                Column += 1
            except:
                Number_of_Seats = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Number_of_Seats
                Column += 1
            
            try:
                Segment =  driver.find_elements(by =By.XPATH, value = "//td[text()='Segment:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Segment
                Column += 1
            except:
                Segment = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Segment
                Column += 1
                
            try:
                Introduction =  driver.find_elements(by =By.XPATH, value = "//td[text()='Introduction:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Introduction
                Column += 1
            except:
                Introduction = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Introduction
                Column += 1
            try:
                End =  driver.find_elements(by =By.XPATH, value = "//td[text()='End:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = End
                Column += 1
            except:
                End = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = End
                Column += 1
            print("General data found.")

            #Drive
            try:
                Drive_Wheel = driver.find_elements(by =By.XPATH, value = "//td[text()='Drive Wheel :']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Drive_Wheel
                Column += 1
            except:
                Drive_Wheel = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Drive_Wheel
                Column += 1
            try:
                Engine_motor_Type = driver.find_elements(by =By.XPATH, value = "//td[text()='Engine/motor Type:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Engine_motor_Type
                Column += 1
            except:
                Engine_motor_Type = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Engine_motor_Type
                Column += 1
            try:
                Fuel_Type = driver.find_elements(by =By.XPATH, value = "//td[text()='Fuel Type:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Fuel_Type
                Column += 1
            except:
                Fuel_Type = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Fuel_Type
                Column += 1
            try:
                Power = driver.find_elements(by =By.XPATH, value = "//td[text()='Power:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Power
                Column += 1
            except:
                Power = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Power
                Column += 1
            try:
                Total_Max_Power_kW = driver.find_elements(by =By.XPATH, value = "//td[text()='Total Max. Power (kW):']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Total_Max_Power_kW
                Column += 1
            except:
                Total_Max_Power_kW = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Total_Max_Power_kW
                Column += 1
            try:
                Total_Max_Power_hp = driver.find_elements(by =By.XPATH, value = "//td[text()='Total Max. Power (hp):']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Total_Max_Power_hp
                Column += 1
            except:
                Total_Max_Power_hp = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Total_Max_Power_hp
                Column += 1
            try:
                Max_Torque = driver.find_elements(by =By.XPATH, value = "//td[text()='Max Torque:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Max_Torque
                Column += 1
            except:
                Max_Torque = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Max_Torque
                Column += 1
            print("Drive data found.")

            #Fuel Engine
            try:
                Cylinders  = driver.find_elements(by =By.XPATH, value = "//td[text()='Cylinders:']/following-sibling::td[@class='col-6 grey']")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Cylinders
                Column += 1
            except:
                Cylinders = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Cylinders
                Column += 1
            try:
                Valves_Per_Cylinder  = driver.find_elements(by =By.XPATH, value = '//td[text()="Valves Per Cylinder:"]/following-sibling::td[@class="col-6"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Valves_Per_Cylinder
                Column += 1
            except:
                Valves_Per_Cylinder = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Valves_Per_Cylinder
                Column += 1
            try:
                Engine_Capacity  = driver.find_elements(by =By.XPATH, value = '//td[text()="Engine Capacity:"]/following-sibling::td[@class="col-6 grey"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Engine_Capacity
                Column += 1
            except:
                Engine_Capacity = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Engine_Capacity
                Column += 1
            try:
                Bore_X_Stroke  = driver.find_elements(by =By.XPATH, value = '//td[text()="Bore X Stroke:"]/following-sibling::td[@class="col-6"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Bore_X_Stroke
                Column += 1
            except:
                Bore_X_Stroke = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Bore_X_Stroke
                Column += 1
            try:
                Compression_Ratio  = driver.find_elements(by =By.XPATH, value = '//td[text()="Compression Ratio:"]/following-sibling::td[@class="col-6 grey"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Compression_Ratio
                Column += 1
            except:
                Compression_Ratio = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Compression_Ratio
                Column += 1
            try:
                Max_Power  = driver.find_elements(by =By.XPATH, value = '//td[text()="Max Power:"]/following-sibling::td[@class="col-6"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Max_Power
                Column += 1
            except:
                Max_Power = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Max_Power
                Column += 1
            try:
                Power_kW  = driver.find_elements(by =By.XPATH, value = '//td[text()="Power (kW):"]/following-sibling::td[@class="col-6 grey"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Power_kW
                Column += 1
            except:
                Power_kW = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Power_kW
                Column += 1
            try:
                Power_hp  = driver.find_elements(by =By.XPATH, value = '//td[text()="Power (hp):"]/following-sibling::td[@class="col-6"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Power_hp
                Column += 1
            except:
                Power_hp = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Power_hp
                Column += 1
            try:
                Max_Power_Rpm  = driver.find_elements(by =By.XPATH, value = '//td[text()="Max. Power Rpm:"]/following-sibling::td[@class="col-6 grey"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Max_Power_Rpm
                Column += 1
            except:
                Max_Power_Rpm = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Max_Power_Rpm
                Column += 1
            try:
                Max_Torque  = driver.find_elements(by =By.XPATH, value = '//td[text()="Max Torque:"]/following-sibling::td[@class="col-6"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Max_Torque
                Column += 1
            except:
                Max_Torque = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Max_Torque
                Column += 1
            try:
                Max_Torque_Rpm  = driver.find_elements(by =By.XPATH, value = '//td[text()="Max Torque Rpm:"]/following-sibling::td[@class="col-6 grey"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Max_Torque_Rpm
                Column += 1
            except:
                Max_Torque_Rpm = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Max_Torque_Rpm
                Column += 1
            try:
                Fuel_System  = driver.find_elements(by =By.XPATH, value = '//td[text()="Fuel System:"]/following-sibling::td[@class="col-6"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Fuel_System
                Column += 1
            except:
                Fuel_System = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Fuel_System
                Column += 1
            try:
                Valve_Actuation  = driver.find_elements(by =By.XPATH, value = '//td[text()="Valve Actuation:"]/following-sibling::td[@class="col-6 grey"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Valve_Actuation
                Column += 1
            except:
                Valve_Actuation = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Valve_Actuation
                Column += 1
            try:
                Turbo  = driver.find_elements(by =By.XPATH, value = '//td[text()="Turbo:"]/following-sibling::td[@class="col-6"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Turbo
                Column += 1
            except:
                Turbo = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Turbo
                Column += 1
            try:
                Catalyst  = driver.find_elements(by =By.XPATH, value = '//td[text()="Catalyst:"]/following-sibling::td[@class="col-6 grey"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Catalyst
                Column += 1
            except:
                Catalyst = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Catalyst
                Column += 1
            try:
                Fuel_Tank_Capacity  = driver.find_elements(by =By.XPATH, value = '//td[text()="Fuel Tank Capacity:"]/following-sibling::td[@class="col-6"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Fuel_Tank_Capacity
                Column += 1
            except:
                Fuel_Tank_Capacity = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Fuel_Tank_Capacity
                Column += 1
            print("Fuel Engine data found.")

            #Performance
            try:
                Top_Speed = driver.find_elements(by =By.XPATH, value = '//td[text()="Top Speed:"]/following-sibling::td[@class="col-6 grey"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Top_Speed
                Column += 1
            except:
                Top_Speed = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Top_Speed
                Column += 1
            try:
                Acceleration_0_100_Km_H = driver.find_elements(by =By.XPATH, value = '//td[text()="Acceleration 0-100 Km / H:"]/following-sibling::td[@class="col-6"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Acceleration_0_100_Km_H
                Column += 1
            except:
                Acceleration_0_100_Km_H = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Acceleration_0_100_Km_H
                Column += 1
            try:
                Practice_Consumption_Monitor = driver.find_elements(by =By.XPATH, value = '//td[text()="Practice Consumption Monitor:"]/following-sibling::td[@class="col-6 grey"]')[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Practice_Consumption_Monitor
                Column += 1
            except: 
                Practice_Consumption_Monitor = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Practice_Consumption_Monitor
                Column += 1
            print("Performance data found.")

            #Consumption(NEDC)
            try:
                Urban_Consumption = driver.find_elements(by =By.XPATH, value = "//td[text()='Urban Consumption:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Urban_Consumption
                Column += 1
            except:
                Urban_Consumption = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Urban_Consumption
                Column += 1
            try:
                Extra_Urban_Consumption = driver.find_elements(by =By.XPATH, value = "//td[text()='Extra-urban Consumption:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Extra_Urban_Consumption
                Column += 1
            except:
                Extra_Urban_Consumption = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Extra_Urban_Consumption
                Column += 1
            try:
                Combined_Consumption = driver.find_elements(by =By.XPATH, value = "//td[text()='Combined Consumption:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Combined_Consumption
                Column += 1
            except:
                Combined_Consumption = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Combined_Consumption
                Column += 1
            try:
                Co2_Emissions = driver.find_elements(by =By.XPATH, value = "//td[text()='Co2 Emissions:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Co2_Emissions
                Column += 1
            except:
                Co2_Emissions = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Co2_Emissions
                Column += 1
            try:
                Energy_Label = driver.find_elements(by =By.XPATH, value = "//td[text()='Energy Label:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Energy_Label
                Column += 1
            except:
                Energy_Label = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Energy_Label
                Column += 1
            try:
                Power_Consumption = driver.find_elements(by =By.XPATH, value = "//td[text()='Power Consumption:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Power_Consumption
                Column += 1
            except:
                Power_Consumption = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Power_Consumption
                Column += 1
            try:
                Battery_Range = driver.find_elements(by =By.XPATH, value = "//td[text()='Battery Range:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Battery_Range
                Column += 1
            except:
                Battery_Range = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Battery_Range
                Column += 1
            print("Consumption(NEDC) data found.")

            #Consumption(WLTP)
            try:
                Low_Consumption = driver.find_elements(by =By.XPATH, value = "//td[text()='Low Consumption:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Low_Consumption
                Column += 1
            except:
                Low_Consumption = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Low_Consumption
                Column += 1
            try:
                Medium_Consumption = driver.find_elements(by =By.XPATH, value = "//td[text()='Medium Consumption:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Medium_Consumption
                Column += 1
            except:
                Medium_Consumption = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Medium_Consumption
                Column += 1
            try:
                High_Consumption = driver.find_elements(by =By.XPATH, value = "//td[text()='High Consumption:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = High_Consumption
                Column += 1
            except:
                High_Consumption = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = High_Consumption
                Column += 1
            try:
                Very_High_Consumption = driver.find_elements(by =By.XPATH, value = "//td[text()='Very High Consumption:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Very_High_Consumption
                Column += 1
            except:
                Very_High_Consumption = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Very_High_Consumption
                Column += 1
            try:
                Combined_Consumption = driver.find_elements(by =By.XPATH, value = "//td[text()='Combined Consumption:']/following-sibling::td")[1].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Combined_Consumption
                Column += 1
            except:
                Combined_Consumption = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Combined_Consumption
                Column += 1
            try:
                Co2_Emissions = driver.find_elements(by =By.XPATH, value = "//td[text()='Co2 Emissions:']/following-sibling::td")[1].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Co2_Emissions
                Column += 1
            except:
                Co2_Emissions = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Co2_Emissions
                Column += 1
            try:
                Battery_Range = driver.find_elements(by =By.XPATH, value = "//td[text()='Battery Range:']/following-sibling::td")[1].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Battery_Range
                Column += 1
            except:
                Battery_Range = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Battery_Range
                Column += 1
            try:
                Power_Consumption = driver.find_elements(by =By.XPATH, value = "//td[text()='Power Consumption:']/following-sibling::td")[1].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Power_Consumption
                Column += 1
            except:
                Power_Consumption = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Power_Consumption
                Column += 1

            print("Consumption(WLTP) data found.")

            #Chassis
            try:
                Front_Suspension_1 = driver.find_elements(by =By.XPATH, value = "//td[text()='Front Suspension:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Front_Suspension_1
                Column += 1
            except:
                Front_Suspension_1  =""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Front_Suspension_1
                Column += 1
            try:
                Rear_Suspension_1 = driver.find_elements(by =By.XPATH, value = "//td[text()='Rear Suspension:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rear_Suspension_1
                Column += 1
            except:
                Rear_Suspension_1 = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rear_Suspension_1
                Column += 1
            try:
                Front_Suspension_2 = driver.find_elements(by =By.XPATH, value = "//td[text()='Front Suspension:']/following-sibling::td")[1].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Front_Suspension_2
                Column += 1
            except:
                Front_Suspension_2 = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Front_Suspension_2
                Column += 1
            try:
                Rear_Suspension_2 = driver.find_elements(by =By.XPATH, value = "//td[text()='Rear Suspension:']/following-sibling::td")[1].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rear_Suspension_2
                Column += 1
            except:
                Rear_Suspension_2 = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rear_Suspension_2
                Column += 1
            try:
                Front_Stabilizer = driver.find_elements(by =By.XPATH, value = "//td[text()='Front Stabilizer:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Front_Stabilizer
                Column += 1
            except:
                Front_Stabilizer = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Front_Stabilizer
                Column += 1
            try:
                Rear_Stabilizer = driver.find_elements(by =By.XPATH, value = "//td[text()='Rear Stabilizer:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rear_Stabilizer
                Column += 1
            except:
                Rear_Stabilizer = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rear_Stabilizer
                Column += 1
            try:
                Front_Brakes = driver.find_elements(by =By.XPATH, value = "//td[text()='Front Brakes:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Front_Brakes
                Column += 1
            except:
                Front_Brakes = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Front_Brakes
                Column += 1
            try:
                Rear_Brakes = driver.find_elements(by =By.XPATH, value = "//td[text()='Rear Brakes:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rear_Brakes
                Column += 1
            except:
                Rear_Brakes = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rear_Brakes
                Column += 1
            try:
                Front_Tire_Size = driver.find_elements(by =By.XPATH, value = "//td[text()='Front Tire Size:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Front_Tire_Size
                Column += 1
            except:
                Front_Tire_Size = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Front_Tire_Size
                Column += 1
            try:
                Rear_Tire_Size = driver.find_elements(by =By.XPATH, value = "//td[text()='Rear Tire Size:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rear_Tire_Size
                Column += 1
            except:
                Rear_Tire_Size = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rear_Tire_Size
                Column += 1
            try:
                Turning_Circle = driver.find_elements(by =By.XPATH, value = "//td[text()='Turning Circle:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Turning_Circle
                Column += 1
            except:
                Turning_Circle = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Turning_Circle
                Column += 1
            print("Chassis data found.")

            #Transmission
            try:
                First_Gear = driver.find_elements(by =By.XPATH, value = "//td[text()='1st Gear:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = First_Gear
                Column += 1
            except:
                First_Gear = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = First_Gear
                Column += 1
            try:
                Second_Gear = driver.find_elements(by =By.XPATH, value = "//td[text()='2nd Gear:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Second_Gear
                Column += 1
            except:
                Second_Gear = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Second_Gear
                Column += 1
            try:
                Third_Gear = driver.find_elements(by =By.XPATH, value = "//td[text()='3rd Gear:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Third_Gear
                Column += 1
            except:
                Third_Gear  =""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Third_Gear
                Column += 1
            try:
                Fourth_Gear = driver.find_elements(by =By.XPATH, value = "//td[text()='4th Gear:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Fourth_Gear
                Column += 1
            except:
                Fourth_Gear = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Fourth_Gear
                Column += 1
            try:
                Fifth_Gear = driver.find_elements(by =By.XPATH, value = "//td[text()='5th Gear:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Fifth_Gear
                Column += 1
            except:
                Fifth_Gear = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Fifth_Gear
                Column += 1
            try:
                Sixth_Gear = driver.find_elements(by =By.XPATH, value = "//td[text()='6th Gear:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Sixth_Gear
                Column += 1
            except:
                Sixth_Gear = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Sixth_Gear
                Column += 1
            try:
                Seventh_Gear = driver.find_elements(by =By.XPATH, value = "//td[text()='7th Gear:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Seventh_Gear
                Column += 1
            except:
                Seventh_Gear = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Seventh_Gear
                Column += 1
            try:
                Eighth_Gear = driver.find_elements(by =By.XPATH, value = "//td[text()='8th Gear:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Eighth_Gear
                Column += 1
            except:
                Eighth_Gear  = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Eighth_Gear
                Column += 1
            try:
                Ninth_Gear = driver.find_elements(by =By.XPATH, value = "//td[text()='9th Gear:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Ninth_Gear
                Column += 1
            except:
                Ninth_Gear = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Ninth_Gear
                Column += 1
            try:
                Reverse_Gear = driver.find_elements(by =By.XPATH, value = "//td[text()='Reverse Gear:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Reverse_Gear
                Column += 1
            except:
                Reverse_Gear = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Reverse_Gear
                Column += 1
            try:
                Final_Drive = driver.find_elements(by =By.XPATH, value = "//td[text()='Final Drive:']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Final_Drive
                Column += 1
            except:
                Final_Drive = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Final_Drive
                Column += 1
            try: 
                Rpm_At_120_Km_h = driver.find_elements(by =By.XPATH, value = "//td[text()='Rpm At 120 Km/h (theoretical):']/following-sibling::td")[0].text
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rpm_At_120_Km_h
                Column += 1
            except:
                Rpm_At_120_Km_h = ""
                sheet[f"{Column_List[Column]}{str(Row)}"] = Rpm_At_120_Km_h
                Column += 1
            print("Transmission data found")

            print()
            print()
            print(f"{Wbn}. {web_page} data found.")
                

            driver.quit()
            time.sleep(5)
            Column = 0
            Row += 1
            Wbn += 1
    
workbook.save(path = "A:\1 - Study Files\102 - Git Folder & Files Uploader\01 - CO2 Emission Prediction with Azure ML\Azure ML SDK\Data\Scraped_Car_Data.csv")
print("File Saved.")
