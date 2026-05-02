# Kingston Website - Broken Links & Fix List

## Total Broken Links: ~100+

This file contains all the `href="#"` links that need to be fixed across the website.

---

## 🔴 CRITICAL LINKS (High Priority - Fix First)

### Top Header Bar (appears on ALL pages)
```html
<!-- Current (Broken) -->
<a href="#">COE</a>
<a href="#">Grievance & Help Desk</a>
<a href="#">Student-Log In</a>
<a href="#">Staff-Log In</a>
<a href="#">Pay Online</a>

<!-- Suggested Fixes -->
<a href="https://www.gov.in/coe">COE</a> (or internal page if you have one)
<a href="contact_support.html">Grievance & Help Desk</a>
<a href="https://lms.kingston.ac.in">Student-Log In</a> (setup your LMS)
<a href="https://staff-lms.kingston.ac.in">Staff-Log In</a> (setup your LMS)
<a href="https://payment.kingston.ac.in">Pay Online</a> (setup payment gateway)
```

### Main Navigation (Navigation Bar)
```html
<!-- Current (Broken) -->
Navigation > Placements > <a href="#">Placements</a>
Navigation > IQAC > <a href="#">IQAC</a>
Navigation > NAAC > <a href="#">NAAC</a>

<!-- Should Be Changed To -->
Navigation > Placements > <a href="placement_pat.html">Placements</a>
Navigation > IQAC > <a href="iqac_about.html">IQAC</a>
Navigation > NAAC > <a href="naac_ssr.html">NAAC</a>
```

### Floating Buttons (Right side of page)
```html
<!-- These are OK -->
<a href="apply_now.html">Apply Now</a> ✅
<a href="admission_enquiry.html">Admission Enquiry</a> ✅

<!-- But Bottom Buttons Need Fixing -->
<a href="#" class="circle-btn">Chatbot (Robot)</a> ❌
<a href="#" class="circle-btn">WhatsApp</a> ❌

<!-- Suggested Fixes -->
<a href="javascript:openChatbot()" class="circle-btn">Chatbot</a>
<a href="https://wa.me/917540037999" target="_blank" class="circle-btn">WhatsApp</a>
```

---

## 🟠 IMPORTANT LINKS (Medium Priority)

### UGC Content Links
```html
<!-- In UGC/About HEI sections, these need fixing -->
<a href="#">About HEI</a> → <a href="ugc_ps_aboutus.html">About HEI</a>
<a href="#">Administrations</a> → <a href="ugc_ps_about_kingston.html">Administrations</a>
<a href="#">Library</a> → <a href="facilities_library.html">Library</a>
<a href="#">Central Facilities</a> → <a href="#">Central Facilities</a> (needs page)
<a href="#">Job Openings</a> → <a href="#">Job Openings</a> (needs page)
<a href="#">Details and Location Map</a> → <a href="#">Location Map</a> (needs page)
```

### Social Media Links (Footer)
```html
<!-- Current (All Broken) -->
<a href="#"><i class="fa-brands fa-facebook"></i> Facebook</a>
<a href="#"><i class="fa-brands fa-instagram"></i> Instagram</a>
<a href="#"><i class="fa-brands fa-twitter"></i> Twitter</a>
<a href="#"><i class="fa-brands fa-youtube"></i> YouTube</a>

<!-- Should Be Fixed To -->
<a href="https://facebook.com/kingstonec" target="_blank">Facebook</a>
<a href="https://instagram.com/kingston_engineering" target="_blank">Instagram</a>
<a href="https://twitter.com/kingston_eng" target="_blank">Twitter</a>
<a href="https://youtube.com/c/kingstonengineering" target="_blank">YouTube</a>

<!-- Update these URLs with your actual social media handles -->
```

### Footer Quick Links
```html
<!-- Current Status -->
<a href="about.html">About Us</a> ✅
<a href="admission.html">Admissions</a> ✅
<a href="#">Departments</a> → <a href="departments.html">Departments</a>
<a href="#">Academics</a> → <a href="academics.html">Academics</a>
<a href="#">Placements</a> → <a href="placement_pat.html">Placements</a>
```

### Footer Programme Links
```html
<a href="#">B.E. Computer Science</a> → <a href="dept_cse.html">B.E. CS</a>
<a href="#">B.E. Electronics & Comm.</a> → <a href="dept_ece.html">B.E. ECE</a>
<a href="#">B.E. Mechanical</a> → <a href="dept_mechanical.html">B.E. Mechanical</a>
<a href="#">B.E. Civil Engineering</a> → <a href="dept_civil.html">B.E. Civil</a>
<a href="#">B.Tech. Information Technology</a> → <a href="dept_IT.html">B.Tech IT</a>
<a href="#">MBA</a> → <a href="dept_MBA.html">MBA</a>
```

### Footer Bottom Links
```html
<a href="#">Privacy Policy</a> → <a href="privacy_policy.html">Privacy Policy</a>
<a href="#">Sitemap</a> → <a href="sitemap.html">Sitemap</a>
<a href="#">Contact</a> → <a href="#">Contact</a> (needs page or mailto)
```

---

## 🟡 MEDIUM PRIORITY LINKS

### Navigation Dropdown Links
```html
<!-- UGC Section Links -->
<a href="#">About HEI</a>
<a href="#">Administrations</a>
<a href="#">Academic</a>
<a href="#">Admissions</a>
<a href="#">Research's</a>
<a href="#">Student Life</a>
<a href="#">Information Corner</a>

<!-- Should map to actual pages like -->
<a href="ugc_ps_aboutus.html">About HEI</a>
<a href="ugc_ps_about_kingston.html">Administrations</a>
<a href="academics.html">Academic</a>
<a href="admission.html">Admissions</a>
<a href="#">Research</a> (needs page)
<a href="#">Student Life</a> (needs page)
<a href="#">Information Corner</a> (needs page)
```

### Home Link in Navigation
```html
<!-- Current -->
<a href="#" class="active">Home</a>

<!-- Should Be -->
<a href="index.html" class="active">Home</a>
```

---

## 📋 ALL BROKEN LINKS BY FILE

### Appears in EVERY page (140+ files):

1. **Header Links:** ~8 broken links per file
   - COE, Grievance, Student Login, Staff Login, Pay Online
   - Chatbot, WhatsApp circles

2. **Navigation Links:** ~6 broken links per file
   - Home, Placements, IQAC, NAAC
   - UGC submenu items

3. **Footer Links:** ~15 broken links per file
   - Departments, Academics, Placements
   - All 7 program links
   - 4 Social media links
   - Privacy, Sitemap, Contact

**Total Estimated: 140 files × 29 broken links average = ~4,060 broken links total**

---

## ✅ FIX STRATEGY

### Step 1: Create Missing Pages
These pages might not exist yet:
- [ ] Contact page / Contact form
- [ ] Location map page
- [ ] Student life information page
- [ ] Research information page
- [ ] Job openings page
- [ ] More detailed UGC subpages

### Step 2: Create Global Fix (if using PHP/templating)
Instead of fixing all 140 files individually, use PHP includes:

```php
<?php
  // links.php
  define('SITE_URL', 'https://kingston.ac.in');
  define('FACEBOOK', 'https://facebook.com/kingstonec');
  define('INSTAGRAM', 'https://instagram.com/kingston_engineering');
  // etc...
?>

<!-- In each page -->
<?php include 'links.php'; ?>
<a href="<?php echo FACEBOOK; ?>" target="_blank">Facebook</a>
```

### Step 3: Setup External Services
- [ ] Student LMS login portal
- [ ] Staff LMS login portal  
- [ ] Payment gateway (Razorpay, Instamojo, etc.)
- [ ] Chatbot service (Drift, Intercom, etc.)
- [ ] WhatsApp Business API

### Step 4: Update All Files
Use Find & Replace to update:
```
Find: href="#"
Replace with appropriate URLs per section
```

---

## 🎯 Checklist to Complete

- [ ] All header links fixed
- [ ] All navigation links point to correct pages
- [ ] All footer links working
- [ ] All social media links connected
- [ ] Home link works
- [ ] All department/program links working
- [ ] Login pages setup
- [ ] Payment gateway connected
- [ ] Contact form working
- [ ] All pages tested in browser

---

## 🚀 Recommended Link Mapping

```
Header Links:
/
/coe → External or new page
/support → New support page
/student-login → https://lms.kingston.ac.in
/staff-login → https://staff.kingston.ac.in
/pay-online → https://payments.kingston.ac.in

Main Navigation:
/home → index.html
/about → about.html
/academics → academics.html
/admission → admission.html
/departments → departments.html
/placements → placement_pat.html
/iqac → iqac_about.html
/naac → naac_ssr.html
/facilities → facilities.html

Footer Links:
/departments → departments.html
/academics → academics.html
/placements → placement_pat.html
/programs/* → dept_*.html
/privacy → privacy_policy.html
/sitemap → sitemap.html
/contact → contact us email or new page

Social:
Facebook: https://facebook.com/[your-page]
Instagram: https://instagram.com/[your-profile]
Twitter: https://twitter.com/[your-handle]
YouTube: https://youtube.com/[your-channel]

Support:
WhatsApp: https://wa.me/917540037999
Email: admission@kingston.ac.in
```

---

## 📈 Progress Tracking

- [x] Identified all broken links ✅
- [ ] Created missing pages
- [ ] Updated header links
- [ ] Updated navigation links  
- [ ] Updated footer links
- [ ] Setup external services
- [ ] Tested all links
- [ ] Ready for production

---

**Total Work Required:** ~100 link updates across 140 pages (or create template system)
**Estimated Time:** 2-4 hours with Find & Replace
**Alternative:** Use PHP templating to fix all at once (recommended)
