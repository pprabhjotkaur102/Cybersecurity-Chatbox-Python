"""
Cybersecurity Awareness Chatbox
A beginner-friendly Python chatbot for cybersecurity awareness.
Run: python chatbox.py
"""

import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

KNOWLEDGE_BASE = {
    "hello": "Hello! I am CyberSafe, your cybersecurity awareness assistant.",
    "hi": "Hi! Ask me about phishing, passwords, malware, Wi-Fi safety, or online security.",
    "phishing": (
        "Phishing is a scam in which attackers use fake emails, texts, or websites "
        "to trick people into sharing information. Check the sender and domain, avoid "
        "unexpected attachments, and open important services using their official app or website."
    ),
    "password": (
        "Use a long, unique password for every account. A password manager can help, "
        "and multi-factor authentication (MFA) adds another layer of protection. Never share "
        "one-time passwords (OTPs)."
    ),
    "malware": (
        "Malware is harmful software, such as viruses, spyware, or ransomware. Keep your "
        "system updated, install software from trusted sources, and use reputable security tools."
    ),
    "ransomware": (
        "Ransomware is malware that can lock or encrypt files and demand payment. Keep offline "
        "or otherwise protected backups, update software, and do not open suspicious attachments."
    ),
    "wifi": (
        "Use WPA2-AES or WPA3 on your home router, change default router credentials, update its "
        "firmware, and avoid sensitive activity on untrusted public Wi-Fi. HTTPS helps protect "
        "data in transit but does not make every website trustworthy."
    ),
    "url": (
        "To assess a suspicious URL, check the exact domain spelling, be cautious of shortened "
        "links and unexpected messages, and do not enter credentials if unsure. You can navigate "
        "to the organisation's official website directly instead."
    ),
    "two factor": (
        "Multi-factor authentication asks for an additional proof beyond a password. An authenticator "
        "app or security key is generally safer than SMS where supported. Never approve a login you did not start."
    ),
    "otp": "Never share an OTP or verification code with anyone, even someone claiming to be support.",
    "backup": "Keep regular backups of important files and test that you can restore them. Keep at least one backup protected from your everyday device.",
    "update": "Install operating-system, browser, and application updates promptly because they often fix security vulnerabilities.",
    "hacked": (
        "If an account may be compromised, use a trusted device to change its password, sign out other sessions, "
        "enable MFA, review recovery details, and contact the service's official support. If financial information "
        "is involved, contact your bank promptly."
    ),
    "cybersecurity": (
        "Cybersecurity is the practice of protecting devices, networks, applications, and data from unauthorised "
        "access, damage, or theft."
    ),
    "safe browsing": (
        "Keep your browser updated, verify website domains, download files only from trusted sources, "
        "avoid unexpected pop-ups, and never ignore browser security warnings."
    ),
    "contact": (
        "For a real incident, contact the affected service through its official support channel. In India, "
        "you can report cybercrime at the official portal cybercrime.gov.in; for immediate financial cyber fraud, "
        "use the official helpline 1930 as soon as possible."
    ),
    "help": (
        "Topics I can explain: cybersecurity, phishing, password, malware, ransomware, Wi-Fi, URL, "
        "two factor, OTP, backup, update, hacked, safe browsing, and contact."
    ),
}

def get_reply(message: str) -> str:
    text = message.lower().strip()
    if not text:
        return "Please type a question."
    if text in {"bye", "exit", "quit"}:
        return "Goodbye! Stay safe online."
    # Prefer longer phrases so that "two factor" is matched before shorter terms.
    for keyword in sorted(KNOWLEDGE_BASE, key=len, reverse=True):
        if keyword in text:
            return KNOWLEDGE_BASE[keyword]
    return (
        "I don't have a specific answer for that yet. Type 'help' to see supported topics. "
        "This chatbot provides general awareness information, not a complete security audit."
    )

class CyberSafeChatbox:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberSafe - Cybersecurity Chatbox")
        self.root.geometry("720x600")
        self.root.minsize(520, 440)
        self.root.configure(bg="#eef2f7")

        header = tk.Frame(root, bg="#14213d", padx=16, pady=14)
        header.pack(fill=tk.X)
        tk.Label(
            header, text="CyberSafe", font=("Arial", 20, "bold"),
            fg="white", bg="#14213d"
        ).pack(anchor="w")
        tk.Label(
            header, text="Cybersecurity Awareness Assistant",
            font=("Arial", 10), fg="#dbeafe", bg="#14213d"
        ).pack(anchor="w", pady=(3, 0))

        self.chat = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 11),
            bg="white", fg="#172033", padx=12, pady=12
        )
        self.chat.pack(fill=tk.BOTH, expand=True, padx=14, pady=14)
        self.chat.tag_config("user", foreground="#1d4ed8", font=("Arial", 11, "bold"))
        self.chat.tag_config("bot", foreground="#15803d", font=("Arial", 11, "bold"))
        self.chat.tag_config("time", foreground="#64748b", font=("Arial", 8))

        bottom = tk.Frame(root, bg="#eef2f7", padx=14, pady=(0, 14))
        bottom.pack(fill=tk.X)
        self.entry = tk.Entry(bottom, font=("Arial", 11), relief=tk.SOLID, bd=1)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10, padx=(0, 8))
        self.entry.bind("<Return>", self.send_message)
        tk.Button(
            bottom, text="Send", command=self.send_message,
            bg="#2563eb", fg="white", activebackground="#1d4ed8",
            activeforeground="white", font=("Arial", 10, "bold"),
            relief=tk.FLAT, padx=18, pady=9
        ).pack(side=tk.RIGHT)

        self.add_message("CyberSafe", "Hello! Ask me about cybersecurity. Type 'help' for topics.")
        self.entry.focus_set()

    def add_message(self, speaker, message):
        timestamp = datetime.now().strftime("%H:%M")
        self.chat.configure(state=tk.NORMAL)
        tag = "user" if speaker == "You" else "bot"
        self.chat.insert(tk.END, f"{speaker} ", tag)
        self.chat.insert(tk.END, f"{timestamp}\n", "time")
        self.chat.insert(tk.END, f"{message}\n\n")
        self.chat.configure(state=tk.DISABLED)
        self.chat.see(tk.END)

    def send_message(self, event=None):
        message = self.entry.get().strip()
        if not message:
            return
        self.entry.delete(0, tk.END)
        self.add_message("You", message)
        reply = get_reply(message)
        self.add_message("CyberSafe", reply)

if __name__ == "__main__":
    window = tk.Tk()
    app = CyberSafeChatbox(window)
    window.mainloop()
