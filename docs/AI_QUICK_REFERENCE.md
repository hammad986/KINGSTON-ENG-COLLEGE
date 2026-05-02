# ⚡ QUICK REFERENCE - AI ASSISTANT SETUP

## 📍 Files Location

| File | Purpose | Location |
|------|---------|----------|
| Knowledge Base | All college data (JSON) | `data/knowledge-base.json` |
| AI Engine | Smart response generator | `assets/js/ai-assistant.js` |
| AI Page | Dedicated chat interface | `ai-assistant.html` |
| Header Template | Reusable header code | `HEADER_TEMPLATE.html` |
| Setup Guide | Complete implementation | `AI_ASSISTANT_SETUP_GUIDE.md` |
| This File | Quick reference | `AI_QUICK_REFERENCE.md` |

---

##🚀 3-Step Setup for Any Page

### **Step 1: Copy HTML to `<body>`**
```html
<!-- Floating AI Button -->
<div class="floating-circle-buttons">
    <a href="ai-assistant.html" class="circle-btn bg-brand-blue ai-widget-toggle">
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
                <input type="text" id="ai-input" class="ai-input" placeholder="Ask me anything...">
                <button id="ai-send-btn" class="ai-send-btn"><i class="fa-solid fa-paper-plane"></i></button>
            </div>
        </div>
    </div>
</div>
```

### **Step 2: Copy CSS to `<style>` in `<head>`**

Copy all `.ai-*` styles from `HEADER_TEMPLATE.html` (search for `/* AI Widget Styles */`)

### **Step 3: Add Script Before `</body>`**
```html
<script src="assets/js/ai-assistant.js" defer></script>
```

**Done!** ✅ Page now has AI assistant

---

## 💬 What Users Can Ask

| Type | Examples |
|------|----------|
| **Admissions** | "How to apply?", "What's the cutoff?", "Eligibility?" |
| **Departments** | "Tell me about CSE", "IT vs EC?", "AI&DS course" |
| **Placements** | "Placement rate?", "Companies?", "Salary range?" |
| **Facilities** | "Hostels?", "Labs?", "Library?", "Sports?" |
| **Contact** | "Phone number?", "Email?", "Address?", "How to reach?" |
| **Navigation** | "How to apply?", "Where's FAQ?", "Show campus tour?" |

---

## 🤖 AI Response Examples

### Example 1:
```
User: Tell me about placements
Bot: 📊 Kingston Placement Statistics:
     ✅ Placement Rate: 95%
     💰 Average Package: ₹6.5 LPA
     🏆 Highest Package: ₹25 LPA
     🏢 Recruiting Companies: 50+
     📍 Placement Cell: placement_pat.html
```

### Example 2:
```
User: What are hostel facilities?
Bot: 🛏️ Hostel Facilities:
     ✅ Capacity: 2000+ students
     🔑 Room Types: Single, Dual, Triple
     📡 WiFi: High-speed internet
     🍽️ Mess: 3 meals daily
     🔒 Security: 24x7 CCTV & staff
```

### Example 3:
```
User: mujhe CS department batao
Bot: 🎓 Computer Science and Engineering (CSE)
     📚 Duration: 4 years
     👥 Seats: 180
     📝 Description: Core CS with programming, data structures...
```

---

## 🎯 Robot Button Actions

**Desktop View:**
- Click = Opens AI widget with chat interface
- Close (X) = Hides widget

**Mobile View:**
- Click = Opens AI widget
- Option to expand to full page
- Chat, send message, explore suggestions

---

## 📊 AI Knowledge Base Contents

### **Departments (10 total)**
- Computer Science & Engineering (180 seats)
- Electronics & Communication (120 seats)
- Mechanical Engineering (120 seats)
- Information Technology (120 seats)
- Civil Engineering (90 seats)
- AI & Data Science (60 seats)
- CSE with AI & ML (60 seats)
- Computer Science & Business Systems (60 seats)
- Bachelor of Architecture (40 seats)
- MBA (120 seats)

### **Key Statistics**
- 95% placement rate
- ₹6.5 LPA average package
- ₹25 LPA highest package
- 50+ recruiting companies

### **Campus Landmarks**
- Main Building (45+ smart classrooms)
- 12 Computer Labs (600+ systems, 24x7 access)
- Central Library (50,000+ books, online databases)
- Sports Complex (10 acres, 8 sports)
- Hostels (2000+ capacity)
- Cafeteria (800+ seating, multi-cuisine)

---

## 🔄 Update Knowledge Base

### **To Add New Information:**

1. Open `data/knowledge-base.json`
2. Add entry under appropriate section
3. Example - Add FAQ:
```json
{
  "category": "departments",
  "question": "What is AI&DS?",
  "answer": "AI & Data Science program focuses on machine learning..."
}
```

### **Reload Required:**
- Just refresh the page
- AI automatically uses updated data

---

## 🎨 Customization

### **Change Widget Colors:**
In `ai-assistant.js`, line ~50:
```javascript
background: linear-gradient(135deg, #003366, #1a5490);
// Change hex colors to your preference
```

### **Change Placeholder Text:**
In HTML:
```html
<input placeholder="Ask about Kingston...">
```

### **Add More FAQs:**
In `knowledge-base.json`, add to `faq_data` array:
```json
{
  "category": "facilities",
  "question": "Is WiFi available?",
  "answer": "Yes, 100 Mbps WiFi across campus!"
}
```

---

## ✅ Testing Checklist

After adding to a page:
- [ ] Page loads without errors
- [ ] Robot icon visible (bottom-right)
- [ ] Click robot icon = widget opens
- [ ] Can type in input field
- [ ] Send button responsive
- [ ] AI responds with message
- [ ] Multiple messages show as conversation
- [ ] X button closes widget
- [ ] Works on mobile
- [ ] Widget doesn't block page content

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Widget not showing | Add widget HTML to body, load CSS |
| No responses | Check `assets/js/ai-assistant.js` is loaded |
| Knowledge base empty | Verify `data/knowledge-base.json` path |
| Styling off | Copy all CSS from template |
| Robot icon missing | Add floating-circle-buttons div |

---

## 📱 Responsive Behavior

| Device | Widget Size | Position |
|--------|------------|----------|
| Desktop (1920px) | 350px wide | Bottom-right |
| Tablet (1024px) | 90% width | Bottom-right |
| Mobile (480px) | 90% width | Bottom |

**Automatically adapts to screen size!**

---

## 🔗 Important Links

- **Dedicated AI Page:** `http://yoursite.com/ai-assistant.html`
- **Robot Button Link:** Links to `ai-assistant.html`
- **Knowledge Base:** `data/knowledge-base.json`
- **AI Engine:** `assets/js/ai-assistant.js`

---

## 📞 Core AI Functions

```javascript
// Main functions in ai-assistant.js:

AIAssistant.generateResponse() // Main AI logic
AIAssistant.matchesKeyword()   // Keyword detection
AIAssistant.displayMessage()   // Show in chat
AIAssistant.sendMessage()      // Handle user input

// Response methods:
getAdmissionInfo()      // Admission Q&A
getDepartmentInfo()     // Department details
getPlacementInfo()      // Placement stats
getFacilitiesInfo()     // Campus facilities
getContactInfo()        // Contact details
getAboutInfo()          // About college
getNavigationHelp()     // Page navigation
getFAQAnswer()          // FAQ answers
```

---

## 🎓 For Students

**How to Use:**
1. Click robot icon anywhere on Kingston website
2. Type your question in plain English or Hindi
3. Get instant answer with relevant links
4. Click suggested action or navigate to page

**Example Questions:**
- "Tell me about placement"
- "CSE vs IT kaunsa better hai?"
- "Hostel facilities kya hain?"
- "Contact number"

---

## 👨‍💼 For Administrators

**Monitor AI Usage:**
- conversation history stored in `conversationHistory` array
- Check browser console for logs
- Review `knowledge-base.json` for data coverage

**Update Knowledge:**
- Edit `knowledge-base.json` directly
- No deployment needed
- Changes live after page refresh

**Track Missing Info:**
- If users ask something not in DB, AI gives generic response
- Add to knowledge base to improve response

---

## 🚀 Deploy to All Pages - Batch Instructions

### **One-By-One (Manual):**
1. Open page HTML
2. Add 3 components (HTML, CSS, Script)
3. Test
4. Move to next page

### **Automation (Script):**
Could create Python/Node script to:
1. Find all `.html` files
2. Insert header template
3. Add AI widget
4. Load AI script
5. Test automatically

**Time Estimate:** 2-3 hours manual, 30 mins automated

---

## ✨ AI Assistant Highlights

✅ **Local First** - No internet needed  
✅ **Privacy** - Data stays on browser  
✅ **Fast** - JSON responses < 100ms  
✅ **Smart** - Keyword matching + formatting  
✅ **Helpful** - Suggests page links  
✅ **Bilingual** - Handles Hindi & English  
✅ **Responsive** - Works on all devices  
✅ **Beautiful** - Modern UI with animations  

---

## 📞 Need Help?

1. **Setup Issues?** → Check `AI_ASSISTANT_SETUP_GUIDE.md`
2. **Want to customize?** → Edit `knowledge-base.json` & `ai-assistant.js`
3. **Add to page?** → Follow 3-Step Setup above
4. **Troubleshoot?** → Check Troubleshooting table

---

*Quick Reference | Kingston AI Assistant | March 2026*

