from collections import Counter
from tkinter import *


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        i = self.head
        while i.next:
            i = i.next
        node = Node(data, None)
        i.next = node

    def name_count(self, n1, n2):
        n3 = n1 + n2
        n = Counter(n3)
        count = 0
        for a, num in n.items():
            if num == 1:
                count += 1
        return count

    def circular(self):
        i = self.head
        while i.next:
            i = i.next
        i.next = self.head

    def flames(self, c):
        i = Node(None, self.head)
        for j in range(5):
            for k in range(c - 1):
                i = i.next
            i.next = i.next.next
        return i.data

    def print(self):
        i = self.head
        s = ""
        while i:
            s += str(i.data)
            i = i.next
        print(s)


if __name__ == '__main__':
    d = {"F": "Friend", "L": "Lover", "A": "Affection", "M": "Marriage", "E": "Enemy", "S": "Sister"}
    ll = LinkedList()
    ll.insert_at_end("F")
    ll.insert_at_end("L")
    ll.insert_at_end("A")
    ll.insert_at_end("M")
    ll.insert_at_end("E")
    ll.insert_at_end("S")
    ll.print()
    ll.circular()
    global n1, n2, count


    def answer(n1, n2):
        top = Toplevel()
        top.configure(bg="black")
        global count
        count = ll.name_count(n1, n2)
        Label(top, text=" The names are " + n1 + " and " + n2, fg="white", bg="black", font=("Harlow Solid Italic", 50),
              padx=40,
              pady=50).pack()
        a = ll.flames(count)
        Label(top, text="The match is \n\n" + a + " : " + d[a], fg="white", bg="black", font=("Harlow Solid Italic", 50), padx=40,
              pady=50).pack(pady=50)


    def names():
        Label(w, text=" Enter name 1: ", fg="white", bg="black", font=("Harlow Solid Italic", 30), padx=40,
              pady=30).pack()
        e1 = Entry(w, width=50, bg="white", font=("Times", 15), justify="center")
        e1.pack()
        Label(w, text=" Enter name 2: ", fg="white", bg="black", font=("Harlow Solid Italic", 30), padx=40,
              pady=30).pack()
        e2 = Entry(w, width=50, bg="white", font=("Times", 15), justify="center")
        e2.pack()
        Button(w, text="Submit", fg="white", bg="maroon", font=("Harlow Solid Italic", 15), padx=50, pady=15,
               command=lambda: answer(e1.get(), e2.get())).pack(pady=20)


    w = Tk()
    w.configure(bg="black")
    w.title("FLAMES")

    Label(w, text="f l a m e s", fg="white", bg="black", font=("Harlow Solid Italic", 75), padx=40, pady=20).pack()
    Button(w, text="start", fg="white", bg="maroon", font=("Harlow Solid Italic", 15), padx=50, pady=15,
           command=names).pack()

    w.mainloop()
    print(ll.flames(count))
