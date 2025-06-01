import pywhatkit as kit
import asyncio
import openpyxl
# File paths
file_path = "C:\\Users\\Kunal Talwar\\Downloads\\Elektron\\Contacts.xlsx"
image_path = "C:\\Users\\Kunal Talwar\\Downloads\\Elektron\\Shop Banner.jpg"
# Load the Excel file
workbook = openpyxl.load_workbook(file_path)
sheet = workbook['Corrected']

async def send_whatsapp_message(row, col, image_path):
   try:
       # Read phone number and name
       phone = sheet.cell(row=row, column=col).value
       # Skip rows with missing phone numbers
       if phone is None:
           print(f"Row {row}: Missing phone number. Skipping...")
           return
       # Ensure phone number is a valid string
       phone = "+91" + str(phone).strip()
       # Construct the message
       message = f"Please support Kunal"
       # Debugging: Print details being sent
       print(f"Sending to: {phone}, Message: {message}, Image: {image_path}")
       # Send WhatsApp message with image
       kit.sendwhats_image(receiver=phone, img_path=image_path, caption=message, wait_time=120, tab_close=True)
       print(f"Message and image sent to {phone}")
       # Pause to respect rate limits
       await asyncio.sleep(5)
   except Exception as e:
       print(f"Failed to send message to {phone if 'phone' in locals() else 'Unknown'}: {e}")

async def main():
   # Adjust the range according to your Excel data
   tasks = []
   for col in range(6, 8):  # Columns 5 to 10 (inclusive)
       print(f"Starting messages for Column {col}...")
       for row in range(2, 4):
        tasks.append(send_whatsapp_message(row, col, image_path))
   # Run all tasks concurrently with rate limiting
   await asyncio.gather(*tasks)

if __name__ == "__main__":
   asyncio.run(main())
