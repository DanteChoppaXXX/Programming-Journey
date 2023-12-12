#!./env/bin/python3
# Import necessary libraries
import telebot
import nmap

# Initialize your Telegram bot with the obtained API token
bot = telebot.TeleBot('6519316527:AAF6hjf8GJA3oNjs9VM-9C4D6IuxMAAoOG0')


@bot.message_handler(commands=["/start"]) 
def handle_start(message):
    bot.reply_to(message, "Welcome! This bot can run Nmap scans.")


# Define the command for initiating the Nmap scan
@bot.message_handler(commands=['start_scan'])
def handle_start_scan(message):
    # Extract the target host from the user's message
    target_host = message.text.split()[1]
    
    # Initialize Nmap scanner
    nm = nmap.PortScanner()

    # Perform the Nmap scan with specified flags
    scan_results = nm.scan(hosts=target_host, arguments='-A -sT -sV')

    # Save the results in a text file
    with open('scan_results.txt', 'w') as file:
        file.write(str(scan_results))

    # Respond to the user
    bot.send_message(message.chat.id, f"Nmap scan completed. Results saved in scan_results.txt")

# Start the bot
bot.polling()
