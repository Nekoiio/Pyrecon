# pyStalk 🚨 - A Simple OSINT Tool

`pyStalk` is a **simple** OSINT (Open Source Intelligence). Whether you're a cybersecurity pro, researcher, or curious about a username across the web, this tool has got you covered! 🔍🌐

---

## 🚀 Features

- **Multiple Platforms**: Check usernames across platforms like GitHub, Twitter, Instagram, YouTube, LinkedIn, and more! 📱💻
- **Instant Feedback**: Get real-time results on availability 🟢🔴
- **Easy to Extend**: Add new platforms easily in the `platforms` dictionary 🛠️
- **Lightweight**: Simple to set up and run 🏃‍♂️💨
- **Colorful Output**: Enjoy colorful, user-friendly terminal output 🌈

---

## 🧑‍💻 Requirements

- **Python 3.x** 🔵
- **pip** (Python package manager) 📦

---

## 🔧 Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/pyStalk.git
cd pyStalk
```

### 2. Install Dependencies

Run the `setup.sh` script to automatically install the required dependencies and set up the program:

```bash
chmod +x setup.sh
./setup.sh
```

This will:
- Install Python 3.x and `pip` if needed.
- Install the required packages (`requests` and `colorama`).
- Make `pyStalk` available globally on your system 🔥

### 3. Running the Program

Once the setup is complete, you can use `pyStalk` from anywhere in your terminal! 🎉

#### To scan:

```bash
pystalk --user <username>
pystalk --email <email>
pystalk --domain <domain>
pystalk --meta <file>
```

---

## 🛠️ How It Works

- Depending on the platform's response (200 for found, 404 for not found), the program tells you if the username is available.
- The results are color-coded for clarity:
  - 🟢 **Found**:  exists
  - 🔴 **Not Found**: Username does not exist
  - 🟡 **Error**: Something went wrong!

---

## 🌍 Supported Platforms

Here are some platforms you can check with `pyStalk`:

- **GitHub** 💻
- **Reddit** 🧑‍🤝‍🧑
- **Twitter** 🐦
- **Instagram** 📸
- **TikTok** 🎵
- **Pinterest** 📌
- **SoundCloud** 🎶
- **Medium** ✍️
- **DeviantArt** 🎨
- **Twitch** 🎮
- **YouTube** 📺
- **LinkedIn** 🧑‍💼
- **Facebook** 📱
- **Flickr** 📷
- **WhatsApp** 💬
- **Clubhouse** 🗣️
- **Quora** ❓
- **Slack** 💼
- **Behance** 🖌️
- **500px** 🖼️
- **Steemit** 💸
- **Ask.fm** ❓
- **LiveJournal** 📝
- **Xing** 🧑‍💻
- **Foursquare** 📍
- **Goodreads** 📚
- **Ravelry** 🧶
- **Twitch Clips** 🎥
