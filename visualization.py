import tkinter as tk
import kafka

class KafkaUI:
    def __init__(self, master, topic):
        self.master = master
        self.topic = topic

        # set up Kafka consumer
        self.consumer = kafka.KafkaConsumer(topic)

        # create message display area
        self.message_display = tk.Text(master, height=10, width=50)
        self.message_display.pack()

        # start listening for messages
        self.listen_for_messages()

    def listen_for_messages(self):
        for message in self.consumer:
            # clear display before displaying new message
            self.message_display.delete('1.0', tk.END)

            # display message in UI
            self.message_display.insert(tk.END, message.value)

            # update UI
            self.master.update()

if __name__ == "__main__":
    # create Tkinter window
    root = tk.Tk()

    # set window title
    root.title("Kafka UI")

    # create KafkaUI instance
    kafka_ui = KafkaUI(root, "message_stream")

    # run Tkinter window
    root.mainloop()