# 📺 AI ASSISTANT - VISUAL SETUP GUIDE

This guide shows you exactly how to set up AI on any page with screenshots/steps.

---

## 🎬 SETUP VIDEO TRANSCRIPT

### **Scene 1: Understanding the System**

```
Narrator: Kingston Engineering College now has an AI Assistant system!

What is it?
  • Intelligent chatbot (powered by local AI)
  • Available on every page
  • Answers questions about college
  • No internet required

Why is it useful?
  • Students get instant answers
  • Parents find information easily
  • Reduces support requests
  • Always available (24/7)
```

### **Scene 2: How It Looks**

```
BEFORE:
```
```
Page Layout
├─ Header
├─ Navigation
├─ Content
└─ Footer
```
```

AFTER (Same page + AI):
```
Page Layout
├─ Header
├─ Navigation
├─ Content
├─ Footer
└─ 🤖 Floating AI Widget (bottom-right)
     ├─ Chat messages
     ├─ Input field
     └─ Send button
```
```

### **Scene 3: Step-by-Step Setup**

```
STEP 1: Open Your HTML Page
┌─────────────────────────────────┐
│ <body>                          │
│   ... existing content ...      │
│ </body>                         │
└─────────────────────────────────┘

STEP 2: Add AI Widget HTML
┌─────────────────────────────────┐
│ <body>                          │
│   ... existing content ...      │
│                                 │
│   [PASTE: AI Widget HTML]       │
│   [Copy from HEADER_TEMPLATE]   │
│                                 │
│ </body>                         │
└─────────────────────────────────┘

STEP 3: Add AI CSS  
┌─────────────────────────────────┐
│ <head>                          │
│   ...                           │
│   <style>                       │
│     ... existing styles ...     │
│     [PASTE: AI Widget CSS]      │
│   </style>                      │
│ </head>                         │
└─────────────────────────────────┘

STEP 4: Add AI Script
┌─────────────────────────────────┐
│ </body>                         │
│   ... scripts ...               │
│   [ADD THIS LINE]               │
│   <script src="assets/js/      │
│    ai-assistant.js"></script>  │
│ </body>                         │
└─────────────────────────────────┘
```

### **Scene 4: Testing**

```
TEST CHECKLIST:
┌──────────────────────────────────┐
│ 1. Open page in browser        │ ✓
│ 2. See robot icon bottom-right │ ✓
│ 3. Click robot icon            │ ✓
│ 4. Chat widget opens           │ ✓
│ 5. Type message                │ ✓
│ 6. Hit send                    │ ✓
│ 7. AI responds                 │ ✓
│ 8. Check on mobile             │ ✓
└──────────────────────────────────┘
```

### **Scene 5: User Interaction**

```
USER VIEW:

┌────────────────────────────┐
│ Kingston Website           │
├────────────────────────────┤
│                            │
│   [Page Content]           │
│                            │
│                            │
│        🤖 ← Click Here    │
│       (Robot Icon)         │
└────────────────────────────┘

CHAT OPENS:

┌─────────────────────────────────────┐
│ Kingston AI Assistant        [X]    │
├─────────────────────────────────────┤
│ Hi! I'm Kingston AI Assistant.      │
│ I can help with admissions,         │
│ placements, facilities & more!      │
│                                     │
│ You: Tell me about placements       │
│                                     │
│ Bot: 📊 Kingston Placement Stats:   │
│      ✅ 95% placement rate          │
│      💰 ₹6.5 LPA average           │
│      🏢 50+ companies              │
├─────────────────────────────────────┤
│ [Input field] [Send]                │
└─────────────────────────────────────┘
```

---

## 📊 FILES YOU NEED TO WORK WITH

### **Main Files:**

```
data/
  └─ knowledge-base.json ................... College data (JSON)
     └─ Contains: Departments, FAQs, contact, facilities

assets/
  └─ js/
     └─ ai-assistant.js ................... AI Engine (JavaScript)
        └─ Runs on all pages that include it

components/ (or root)
  └─ HEADER_TEMPLATE.html ................ Copy-paste template
     └─ Contains: Widget HTML + CSS

ai-assistant.html ....................... Dedicated chat page
  └─ Full-screen interface for AI chat

index.html ............................. Already updated!
  └─ Example of AI integrated
```

---

## 🎯 COPY-PASTE TEMPLATE

### **COMPLETE HTML TO ADD:**

```html
<!-- Add this to <body> section -->

<!-- Floating AI Button -->
<div class="floating-circle-buttons">
    <a href="ai-assistant.html" class="circle-btn bg-brand-blue ai-widget-toggle" title="AI Assistant">
        <i class="fa-solid fa-robot"></i>
    </a>
</div>

<!-- AI Widget Container -->
<div id="ai-widget-container" class="ai-widget-hidden">
    <div class="ai-widget-box">
        <div class="ai-widget-header">
            <h3><i class="fa-solid fa-robot"></i> Kingston AI Assistant</h3>
            <button class="ai-widget-close" id="ai-widget-close">&times;</button>
        </div>
        <div class="ai-widget-content">
            <div id="ai-messages" class="ai-messages"></div>
            <div class="ai-input-area">
                <input type="text" id="ai-input" class="ai-input" 
                       placeholder="Ask me anything about Kingston...">
                <button id="ai-send-btn" class="ai-send-btn">
                    <i class="fa-solid fa-paper-plane"></i>
                </button>
            </div>
        </div>
    </div>
</div>
```

### **CSS TO ADD:**

```css
/* Add this to <style> in <head> */

/* AI Widget Styles */
.ai-widget-hidden {
    position: fixed;
    bottom: 100px;
    right: 20px;
    width: 350px;
    max-width: 90vw;
    display: none;
    z-index: 999;
    animation: slideUp 0.3s ease-out;
}

.ai-widget-hidden.active {
    display: block;
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.ai-widget-box {
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    height: 500px;
}

.ai-widget-header {
    background: linear-gradient(135deg, #003366, #1a5490);
    color: white;
    padding: 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.ai-widget-header h3 {
    margin: 0;
    font-size: 1rem;
    display: flex;
    gap: 10px;
    align-items: center;
}

.ai-widget-close {
    background: none;
    border: none;
    color: white;
    font-size: 1.5rem;
    cursor: pointer;
}

.ai-widget-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 15px;
    background: #f9f9f9;
}

.ai-messages {
    flex: 1;
    overflow-y: auto;
    margin-bottom: 15px;
}

.ai-message {
    margin-bottom: 10px;
    display: flex;
    gap: 8px;
}

.ai-message.bot {
    justify-content: flex-start;
}

.ai-message.user {
    justify-content: flex-end;
}

.ai-message-text {
    max-width: 70%;
    padding: 10px 12px;
    border-radius: 10px;
    font-size: 0.9rem;
    line-height: 1.4;
}

.ai-message.bot .ai-message-text {
    background: #e8e8f7;
    color: #333;
}

.ai-message.user .ai-message-text {
    background: #003366;
    color: white;
}

.ai-input-area {
    display: flex;
    gap: 8px;
}

.ai-input {
    flex: 1;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 10px;
    font-size: 0.9rem;
    font-family: inherit;
}

.ai-input:focus {
    outline: none;
    border-color: #003366;
}

.ai-send-btn {
    background: #003366;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 15px;
    cursor: pointer;
    transition: all 0.3s;
}

.ai-send-btn:hover {
    background: #1a5490;
}

@media (max-width: 640px) {
    .ai-widget-hidden {
        width: calc(100% - 40px);
        bottom: 80px;
        right: 20px;
    }

    .ai-widget-box {
        height: 400px;
    }
}
```

### **SCRIPT TO ADD:**

```html
<!-- Add before closing </body> tag -->
<script src="assets/js/ai-assistant.js" defer></script>
```

---

## ✅ VERIFICATION STEPS

After adding all 3 components:

```
1. VISUAL CHECK
   ├─ Find robot icon? YES / NO
   ├─ Is it bottom-right? YES / NO
   ├─ Can you click it? YES / NO
   └─ Does widget open? YES / NO

2. FUNCTIONAL CHECK
   ├─ Can type message? YES / NO
   ├─ Can hit send? YES / NO
   ├─ AI responds? YES / NO
   └─ Messages appear? YES / NO

3. MOBILE CHECK
   ├─ Widget visible? YES / NO
   ├─ Can open? YES / NO
   ├─ Can chat? YES / NO
   └─ Responsive? YES / NO

4. BROWSER CHECK
   ├─ Works Chrome? YES / NO
   ├─ Works Firefox? YES / NO
   ├─ Works Safari? YES / NO
   └─ No errors? YES / NO
```

---

## 🚀 BULK UPDATE (All Pages)

If you want to do ALL pages at once:

### **Option 1: Manual (Fastest)**
```
1. Open HEADER_TEMPLATE.html in editor
2. Copy AI widget HTML + CSS
3. For each page:
   - Open webpage
   - Paste HTML in <body>
   - Paste CSS in <style>
   - Add script tag
   - Save
   - Test
   
Time: ~5-10 minutes per page
Total: 12-20 hours for 140 pages
```

### **Option 2: Automated (Fastest)**
```
Create batch script (Python/Node):
1. Find all .html files
2. Insert header template
3. Add AI widget automatically
4. Load AI script
5. Test each page

Time: 30 minutes setup
Total: 5-10 minutes runtime for all pages
```

---

## 📱 RESPONSIVE BEHAVIOR

### **Desktop (1920px)**
```
┌────────────────────────┐
│ Page Content           │
│                        │
│                        │
│                   🤖   │
│                  ●●●●  │
│ (Widget: 350px wide)   │
└────────────────────────┘
```

### **Mobile (375px)**
```
┌─────────┐
│ Content │
│         │
│         │
│    🤖   │ ← Widget auto-resizes
│    ●●  │
└─────────┘
```

---

## 🎨 CUSTOMIZATION QUICK TIPS

### **Change Colors:**
```javascript
// In ai-assistant.js, find:
background: linear-gradient(135deg, #003366, #1a5490);

// Change to:
background: linear-gradient(135deg, #yourColor1, #yourColor2);
```

### **Change Messages:**
```javascript
// In ai-assistant.js, find displayWelcomeMessage():
"I'm Kingston AI Assistant. I can help you with..."

// Change to your custom message
```

### **Add New FAQs:**
```json
// In knowledge-base.json, add to faq_data:
{
  "category": "your-category",
  "question": "Your question?",
  "answer": "Your answer"
}
```

---

## 🔗 HELPFUL LINKS

**Files to Reference:**
- `HEADER_TEMPLATE.html` ← Copy-paste from here
- `data/knowledge-base.json` ← Manage knowledge here
- `assets/js/ai-assistant.js` ← AI logic here
- `ai-assistant.html` ← Dedicated page here

**Documentation:**
- `AI_ASSISTANT_SETUP_GUIDE.md` ← Full guide
- `AI_QUICK_REFERENCE.md` ← Quick start
- `AI_SETUP_SUMMARY.md` ← Overview

---

## 💡 TROUBLESHOOTING

### **Widget Not Showing?**
```
✓ Did you add HTML?
✓ Did you add CSS?
✓ Is script loading?
✓ Check browser console for errors
```

### **No Responses?**
```
✓ Is knowledge-base.json loading?
✓ Check network tab
✓ Look for 404 errors
✓ Verify JSON path: data/knowledge-base.json
```

### **Mobile not working?**
```
✓ CSS media queries added?
✓ Viewport meta tag present?
✓ Touch events working?
✓ Test on actual device
```

---

## 📊 EXAMPLE: BEFORE & AFTER

### **BEFORE (Without AI):**
```
User visits admission.html
  └─ Reads content
  └─ Doesn't understand something
  └─ Needs to:
     ├─ Scroll to find FAQ page
     ├─ Go through 12 FAQs
     ├─ Or send enquiry & wait
     ├─ Or call phone number
     └─ Takes 5-10 minutes ❌
```

### **AFTER (With AI):**
```
User visits admission.html
  └─ Sees robot icon
  └─ Clicks it
  └─ Types question: "What's the cutoff?"
  └─ Gets instant answer ✅
  └─ Takes 30 seconds ✅
```

---

## 🎯 SUCCESS CRITERIA

After implementing AI:

✅ Widget appears on page
✅ Clicking opens chat
✅ Can type messages
✅ AI responds instantly
✅ Links work in responses
✅ Mobile friendly
✅ No console errors
✅ Conversation continuous

---

## 📞 FINAL CHECKLIST

Before going live:

- [ ] Knowledge base loaded
- [ ] Widget HTML added
- [ ] Widget CSS added
- [ ] Script included
- [ ] Tested on desktop
- [ ] Tested on mobile
- [ ] Robot icon working
- [ ] Chat messages flowing
- [ ] AI responses sensible
- [ ] No console errors
- [ ] Mobile responsive
- [ ] Dedicated page working

---

**Ready to setup AI on all pages?**

Use this guide + HEADER_TEMPLATE.html + 3-step process = Done! 🚀

*Last Updated: March 19, 2026*
