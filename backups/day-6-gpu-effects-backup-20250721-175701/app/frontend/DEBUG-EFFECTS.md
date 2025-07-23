# Debugging GPU Effects

## 🐛 Issue: Effects Not Visible

If you're not seeing the GPU effects, follow these debugging steps:

## 🔍 Step 1: Check Browser Console

1. **Open your browser** and go to: `http://localhost:5173/dashboard`
2. **Open Developer Tools** (F12 or right-click → Inspect)
3. **Go to Console tab**
4. **Look for these messages:**
   ```
   TestEffects: Initializing Three.js scene...
   TestEffects: Renderer added to DOM
   TestEffects: Cube added to scene
   TestEffects: Animation started
   ```

## 🎯 Step 2: Verify Effects Toggle

1. **Look for the purple button** in the top navigation bar
2. **Button should show:** `✨ Effects ON` or `✨ Effects OFF`
3. **Click the button** to toggle effects
4. **You should see a green rotating cube** when effects are ON

## 🔧 Step 3: Check WebGL Support

1. **Go to:** https://get.webgl.org/
2. **Verify your browser supports WebGL**
3. **If not supported, try a different browser**

## 🎨 Step 4: Visual Test

**When effects are working, you should see:**
- ✅ **Green rotating cube** in the background
- ✅ **Dark blue background** behind the cube
- ✅ **Semi-transparent dashboard** over the effects
- ✅ **Smooth 60fps animation**

## 🚨 Common Issues

### Issue 1: No Console Messages
**Problem:** Three.js not loading
**Solution:** Check if Three.js is installed
```bash
cd app/frontend
npm list three
```

### Issue 2: Console Errors
**Problem:** WebGL or Three.js errors
**Solution:** Check browser console for specific error messages

### Issue 3: Effects Toggle Not Working
**Problem:** Button not responding
**Solution:** Check if the component is properly imported

### Issue 4: Performance Issues
**Problem:** Slow or choppy animations
**Solution:** 
- Disable effects using the toggle button
- Check if other tabs are consuming GPU resources

## 🎮 Test Commands

### Check Server Status
```bash
cd app/frontend
npm run dev
```

### Check Three.js Installation
```bash
npm list three @types/three
```

### Check Browser Console
```javascript
// In browser console, type:
console.log('Three.js version:', THREE.REVISION);
```

## 🎯 Expected Behavior

### With Effects ON:
- Green rotating cube visible in background
- Dashboard content semi-transparent
- Smooth animations
- Purple toggle button

### With Effects OFF:
- No 3D effects visible
- Normal dashboard appearance
- Gray toggle button

## 🔄 Switch Back to Full Effects

Once you confirm the test effects are working, we can switch back to the full effects:

1. **Edit:** `app/frontend/src/components/dashboard/Dashboard.tsx`
2. **Change:** `{showEffects && <TestEffects />}` back to `{showEffects && <DashboardEffects />}`
3. **Save and refresh** the page

## 📞 If Still Not Working

1. **Check browser console** for errors
2. **Try a different browser** (Chrome, Firefox, Edge)
3. **Disable browser extensions** that might interfere
4. **Check if your GPU supports WebGL**

## 🎉 Success Indicators

You'll know it's working when you see:
- ✅ Green rotating cube in background
- ✅ Console messages about Three.js initialization
- ✅ Smooth animations without lag
- ✅ Toggle button working properly

Let me know what you see in the browser console and whether the green cube appears! 