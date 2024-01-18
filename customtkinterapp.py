import customtkinter as tk
from discord_webhook import DiscordWebhook

tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")
root = tk.CTk()
root.iconbitmap("./_internal/webhookicon.ico")
root.resizable(False, False)
root.geometry("500x500")
user_input = tk.StringVar(root)
root.title("Webhook Sender")


def sendwebhook():
    try:
        webhook_url = user_input.get()
        message_content = textboxinput.get("0.0", "end")

        if not webhook_url and not message_content.strip():
            succesfullysent.configure(text='Please input a webhook and a text to send')
        elif not webhook_url:
            succesfullysent.configure(text="Input a webhook first")
        elif not message_content.strip():
            succesfullysent.configure(text='Please input some text to send')
        else:
            webhook = DiscordWebhook(webhook_url)
            webhook.content = message_content
            webhook.execute()
            succesfullysent.configure(text='Webhook Message successfully sent!')
    except Exception as e:
        print(f"An error occurred: {e}")
        succesfullysent.configure(text='An error occurred while sending the webhook')




webhooklink = tk.CTkLabel(root, text="Input your webhook link.")
webhooklink.place(relx=0.05, rely=0.1)

entry = tk.CTkEntry(root, width=430, textvariable=user_input)
entry.place(rely=0.15, relx=0.05)

labeltextinput = tk.CTkLabel(root, text="Input your text to send.")
labeltextinput.place(rely=0.22, relx=0.05)

textboxinput = tk.CTkTextbox(root, width=430)
textboxinput.place(relx=0.05, rely=0.27)

textbutton = tk.CTkButton(root, command=sendwebhook, text="Send Webhook")
textbutton.place(rely=0.8, relx=0.34)

credit = tk.CTkLabel(root, text="Made by ThatItalianDude (real)")
credit.place(rely=0.95, relx=0.01)

succesfullysent = tk.CTkLabel(root, text="")
succesfullysent.place(rely=0.7, relx=0.26)

root.mainloop()
