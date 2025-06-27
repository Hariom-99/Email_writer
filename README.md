---

# 📧 Email Writing Bot with Streamlit and Hugging Face

A **smart email-writing assistant** powered by a large language model from Hugging Face and an interactive web interface built with Streamlit. This app helps you generate professional emails of various types (apology, leave request, job application, and more) using bullet-point inputs.

---

## 🚀 Features

✅ Supports multiple email types (apology, leave request, job application, etc.)
✅ Easy bullet-point inputs
✅ Automatically generates well-structured, professional emails
✅ Interactive web interface with a dropdown for email type selection
✅ Works locally or can be deployed to Streamlit Cloud

---

## 🛠️ Tech Stack

* **Python** → main programming language
* **Streamlit** → to create the user-friendly web interface
* **Hugging Face Transformers** → for natural language text generation
* **Flan-T5 Large Model** → a powerful open-source model fine-tuned for text-to-text generation
* **PyTorch** → as the model backend

---

## ⚙️ How It Works

1. **User Input**

   * Select the email type from a dropdown (e.g., apology, leave request, job application)
   * Enter bullet points describing the details of the email (recipient, dates, reason, etc.)

2. **Text Generation**

   * The selected email type and bullet points are combined into a prompt
   * The prompt is sent to the Hugging Face model (`flan-t5-large`)
   * The model returns a professionally structured email

3. **Web Frontend**

   * Streamlit displays the generated email clearly
   * You can copy the output and use it directly

---

## 🧩 Project Structure

```
email_bot.py          # Streamlit app
requirements.txt      # project dependencies
README.md             # project documentation
```

---

## 🌟 Real-Life Use Cases

✅ Customer support teams can quickly draft apology or complaint resolution emails
✅ Employees can generate leave letters without worrying about the format
✅ HR teams can prepare job applications or interview invites faster
✅ Freelancers can generate proposals or follow-up emails
✅ Anyone who struggles with writing professional emails can use this as a personal assistant

---

## 🚀 Getting Started Locally

**Clone this repository:**

```bash
git clone https://github.com/Hariom-99/Email_writer.git
cd Email_writer

```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run the app:**

```bash
streamlit run email_gen.py
```

---

## 🌐 Deployment

Deploy easily to [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push your code to a public GitHub repository
2. Connect your repository on Streamlit Cloud
3. Click **Deploy** and share the generated public link

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve features, fix bugs, or suggest enhancements.

---

## 📄 License

This project is private and does not currently include an open-source license. All rights reserved.

---


