import itchat

@itchat.msg_register(itchat.content.TEXT)
def filter_messages(msg):
    # Example: Filter messages containing "Python"
    if "Python" in msg['Text']:
        print(f"Filtered Message: {msg['Text']}")

itchat.auto_login(hotReload=True)
itchat.run()

# if __name__ == "__main__":
#     main()
#
# def main():



