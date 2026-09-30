import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>EMON | Cloud Gaming Platform</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Hind+Siliguri:wght@500;600;700&display=swap');
    * { font-family: 'Hind Siliguri', sans-serif; }
    .font-orbitron { font-family: 'Orbitron', sans-serif; }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-4 pb-20">

  <div class="max-w-4xl mx-auto space-y-4">
    <!-- Header -->
    <header class="bg-slate-900 border border-cyan-500/30 p-4 rounded-2xl flex justify-between items-center shadow-xl">
      <div>
        <h1 class="text-base sm:text-xl font-black text-cyan-400 font-orbitron">EMON | CLOUD GAMING</h1>
        <p class="text-[11px] text-gray-300 font-semibold">ডেভেলপার: ইমন ইসলাম (Emon Khan)</p>
      </div>
      <div class="bg-emerald-950 text-emerald-400 border border-emerald-500/30 px-3 py-1 rounded-xl text-xs font-bold flex items-center gap-1.5">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span> Server Live
      </div>
    </header>

    <!-- Cloud Gaming Screen / Lobby -->
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 space-y-4 shadow-2xl">
      <div class="relative w-full aspect-video bg-black rounded-xl overflow-hidden border border-slate-700 flex flex-col items-center justify-center p-4 text-center space-y-3 shadow-inner">
        <i class="fa-solid fa-gamepad text-5xl text-cyan-400 animate-bounce"></i>
        <h2 class="text-sm sm:text-base font-bold text-slate-100">ইনস্টল ছাড়াই ব্রাউজারে ব্যাটল রয়্যাল খেলুন</h2>
        <p class="text-xs text-slate-400 max-w-md">পাবজি (PUBG), ফ্রি ফায়ার (Free Fire) এবং অন্যান্য হাই-এন্ড গেম ক্লাউড সার্ভার থেকে সরাসরি স্ট্রিম হবে।</p>
      </div>

      <!-- Game Selection Grid -->
      <div class="grid grid-cols-2 gap-3">
        <div onclick="alert('PUBG Mobile ক্লাউড সার্ভার লোড হচ্ছে...')" class="bg-slate-950 border border-slate-800 hover:border-cyan-500 p-3 rounded-xl cursor-pointer transition text-center space-y-1">
          <i class="fa-solid fa-crosshairs text-amber-400 text-lg"></i>
          <h3 class="text-xs font-bold text-slate-200">PUBG Mobile</h3>
          <p class="text-[10px] text-emerald-400">🟢 সার্ভার ফ্রি</p>
        </div>
        <div onclick="alert('Free Fire ক্লাউড সার্ভার লোড হচ্ছে...')" class="bg-slate-950 border border-slate-800 hover:border-cyan-500 p-3 rounded-xl cursor-pointer transition text-center space-y-1">
          <i class="fa-solid fa-fire text-red-500 text-lg"></i>
          <h3 class="text-xs font-bold text-slate-200">Free Fire MAX</h3>
          <p class="text-[10px] text-emerald-400">🟢 সার্ভার ফ্রি</p>
        </div>
      </div>
    </div>
  </div>

</body>
</html>
"""

@app.get("/")
async def get_index():
    return HTMLResponse(content=HTML_TEMPLATE)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)