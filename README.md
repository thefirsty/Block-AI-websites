# 🧠 AI Website Blocker – Mental Gym Edition

I used to be sharp.  
Then I started “just checking ChatGPT real quick.”  
5 hours later I’d emerge, not smarter — just confused and mildly ashamed.

So I built myself a little tool. A resistance band for the brain.  
Because apparently, thinking is now an extreme sport.

---

## 💪 What Is This?

A small EXE that acts like a personal trainer yelling “NO!”  
at your attempts to open ChatGPT, Bard, Claude, or anything else that wants to “help” you think.

It modifies your hosts file and redirects those tempting AI websites back to the void (a.k.a. 127.0.0.1).

You’ll try to open ChatGPT.  
You’ll fail.  
And then... you might actually think for yourself.

---

## 📌 What It Blocks

Everything from:

chatgpt.com
openai.com
bard.google.com
copilot.microsoft.com
character.ai


All blocked inside your `hosts` file, like this:

```hosts
#ai_blocker_start
127.0.0.1 chatgpt.com
127.0.0.1 openai.com
127.0.0.1 bard.google.com
127.0.0.1 gemini.google.com
127.0.0.1 copilot.microsoft.com
127.0.0.1 claude.ai
127.0.0.1 perplexity.ai
127.0.0.1 character.ai
...
#ai_blocker_end



## 🧠 How to Use This Brain Trainer

### 🟢 To Block AI Sites:
1. Download block_ai_hosts.exe from the [Releases](https://github.com/thefirsty/Block-AI-websites/releases)
2. Right-click → **Run as Administrator**
3. That’s it. You’re now doing mental pushups.

### 🔓 To Unblock (when your boss isn’t watching):
1. Download unblock_ai_hosts.exe
2. Run it as admin
3. All blocked domains will be removed
4. You're back in the AI pool. Swim safely.

---

## ⚠️ System Requirements

🪟 Windows only
🧑‍💻 Must be run **as administrator** (to edit hosts)
No installer. No background watcher. Just one clean shot to the forehead of your productivity parasite.

---

## 🧘 Why?

Because just like your muscles weakened when machines started lifting for you,  
your mind is softening under the warm glow of “AI assistance.”

This is a **digital detox dumbbell**.  
Heavy. Frictional. Beautiful.

---

## 🧰 Built With

🐍 Python 3.13
🪵 loguru – because print() is for interns
🧙 PyInstaller – to turn the idea into a summonable EXE

---

## 🔓 License

MIT – because software freedom should include freedom from software.
