<template>
    <main>
        <section>
          <div class="relative grid w-full bg-indigo-500 h-96 lg:h-[32rem] place-items-center">
            <div class="flex flex-col items-center mx-auto text-center">
              <h1 class="text-4xl font-semibold text-white uppercase md:text-6xl">مدیریت پروژه با آریا</h1>
              <p class="mt-6 text-lg leading-5 text-white">تمامی ابزارهای مورد نیاز شما برای مدیریت پروژه در یک مکان</p>
              
              <div class="mt-8">
                <RouterLink :to="{name:'register'}" class="bg-white text-black py-3 px-6 ml-4 rounded-md text-xl hover:bg-gray-100">ثبت‌نام</RouterLink>
                <RouterLink :to="{name:'login'}" class="bg-white text-black py-3 px-6 rounded-md text-xl  hover:bg-gray-100">ورود</RouterLink>
              </div>
            </div>
          </div>
          <svg class="fill-indigo-500" viewBox="0 0 1440 57" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M1440 0H0V57C720 0 1440 57 1440 57V0Z"></path>
          </svg>
        </section>
      
        <section class="container px-6 py-8 mx-auto lg:py-16" id="about">
          <div class="lg:flex lg:items-center lg:-mx-4">
            <div class="lg:w-1/2 lg:px-4 text-right">
              <h3 class="text-xl font-medium text-gray-800 md:text-2xl lg:text-3xl">مدیریت پروژه‌های خود را با دقت و کارایی بالا انجام دهید</h3>
              <p class="mt-6 text-gray-500">نرم‌افزار ما تمامی امکانات لازم برای مدیریت پروژه، تیم‌های کاری، تسک‌ها و جلسات را در اختیار شما قرار می‌دهد. با امکاناتی همچون ثبت‌نام، ورود، تایید ایمیل، گزارشات دقیق پیشرفت و ... به راحتی می‌توانید پروژه‌های خود را مدیریت کنید.</p>
              <button class="flex items-center mt-8 -mx-2 text-indigo-500" id="register">
                <router-link  class="mx-1 font-semibold" :to="{name:'login'}">شروع کنید</router-link>
              </button>
            </div>
            <div class="mt-8 lg:w-1/2 lg:px-4 lg:mt-0">
              <img class="object-cover w-full rounded-xl h-96" src="/public/img/image.webp" alt="Video thumbnail">
            </div>
          </div>
        </section>
      
        <section class="container px-6 py-12 mx-auto lg:py-20 text-right " dir="rtl">
          <h1 class="text-4xl font-extrabold mb-12 text-indigo-700 text-center">قابلیت‌های برجسته سیستم مدیریت پروژه ما</h1>
        
          <div class="grid grid-cols-1 gap-8 md:grid-cols-2 xl:grid-cols-3">
        
            <div class="p-6 bg-gradient-to-r from-indigo-600 to-purple-600 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">مدیریت دسترسی و دعوت</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M18 20v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
                  <circle cx="9" cy="7" r="4"/>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                </svg>
              </div>
              <p class="text-sm">تعریف نقش‌های مختلف (مدیر، کارمند ارشد، کارمند عادی)، برچسب‌گذاری، دعوت از کاربران با ایمیل.</p>
            </div>
        
            <div class="p-6 bg-gradient-to-r from-green-500 to-emerald-500 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">تسک‌منیجمنت و امتیازدهی</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M9 12h6"/>
                  <path d="M9 16h6"/>
                  <path d="M9 8h6"/>
                  <circle cx="6" cy="12" r="1"/>
                  <circle cx="6" cy="16" r="1"/>
                  <circle cx="6" cy="8" r="1"/>
                </svg>
              </div>
              <p class="text-sm">تعریف، تمدید، تعیین شخص تحویل‌دهنده، وضعیت تسک، امتیازدهی و بازخورد هوشمند.</p>
            </div>
        
            <div class="p-6 bg-gradient-to-r from-yellow-500 to-orange-400 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">نمای تقویمی</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                  <line x1="16" y1="2" x2="16" y2="6"/>
                  <line x1="8" y1="2" x2="8" y2="6"/>
                  <line x1="3" y1="10" x2="21" y2="10"/>
                </svg>
              </div>
              <p class="text-sm">نمایش تسک‌ها به‌صورت تقویمی برای درک بهتر زمان‌بندی و اولویت‌بندی.</p>
            </div>
        
            <div class="p-6 bg-gradient-to-r from-pink-500 to-rose-500 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">گفت‌و‌گو و پشتیبانی</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17 8h2a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2h-2"/>
                  <path d="M7 8H5a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/>
                  <rect x="7" y="4" width="10" height="4" rx="1"/>
                  <line x1="12" y1="12" x2="12" y2="18"/>
                  <line x1="9" y1="15" x2="15" y2="15"/>
                </svg>
              </div>
              <p class="text-sm">قابلیت گفتگو در تسک، وضعیت گفتگو (باز/بسته)، پاسخ توسط دیگر کاربران و پیوست فایل.</p>
            </div>
        
            <div class="p-6 bg-gradient-to-r from-blue-600 to-sky-500 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">نصب اپلیکیشن PWA</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 20h9"/>
                  <path d="M12 4h9"/>
                  <path d="M12 12h9"/>
                  <path d="M3 7a4 4 0 0 1 4-4h1"/>
                  <path d="M3 17a4 4 0 0 0 4 4h1"/>
                  <circle cx="6.5" cy="12" r="2.5"/>
                </svg>
              </div>
              <p class="text-sm">تبدیل پروژه به اپلیکیشن موبایلی با قابلیت نصب روی دسکتاپ یا تلفن همراه.</p>
            </div>
        
            <div class="p-6 bg-gradient-to-r from-cyan-500 to-teal-500 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">پوش و ایمیل نوتیفیکیشن</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M15 17h5l-1.405-1.405"/>
                  <path d="M19 13v-2a7 7 0 0 0-14 0v2"/>
                  <path d="M10 21h4"/>
                  <circle cx="12" cy="12" r="9"/>
                </svg>
              </div>
              <p class="text-sm">ارسال اعلان‌های لحظه‌ای از طریق مرورگر و ایمیل جهت اطلاع‌رسانی تسک‌ها و رویدادها.</p>
            </div>
        
            <div class="p-6 bg-gradient-to-r from-fuchsia-600 to-pink-600 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">چارت‌های پیشرفت پروژه</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 20h9"/>
                  <path d="M12 4h9"/>
                  <path d="M12 12h9"/>
                  <path d="M3 7a4 4 0 0 1 4-4h1"/>
                  <path d="M3 17a4 4 0 0 0 4 4h1"/>
                  <circle cx="6.5" cy="12" r="2.5"/>
                </svg>
              </div>
              <p class="text-sm">نمایش درصد پیشروی پروژه بر اساس تسک‌های انجام‌شده به شکل گراف‌های ماهانه.</p>
            </div>
        
            <div class="p-6 bg-gradient-to-r from-red-500 to-orange-500 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">لندینگ پیج معرفی محصول</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 8h18"/>
                  <path d="M3 16h18"/>
                  <path d="M7 8v8"/>
                  <path d="M17 8v8"/>
                </svg>
              </div>
              <p class="text-sm">طراحی حرفه‌ای صفحه معرفی محصول برای جذب کاربر و معرفی امکانات پروژه.</p>
            </div>
        
            <div class="p-6 bg-gradient-to-r from-violet-600 to-indigo-500 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">دسته‌بندی و اهمیت</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"/>
                  <line x1="15" y1="9" x2="9" y2="15"/>
                  <line x1="9" y1="9" x2="15" y2="15"/>
                </svg>
              </div>
              <p class="text-sm">دسته‌بندی تسک‌ها، تعیین اهمیت (بالا، متوسط، پایین) برای مدیریت بهینه وظایف.</p>
            </div>
        
            <div class="p-6 bg-gradient-to-r from-lime-500 to-green-400 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">پیوست فایل به تسک</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14 2 14 8 20 8"/>
                </svg>
              </div>
              <p class="text-sm">قابلیت ضمیمه‌کردن فایل‌ها، تصاویر و اسناد به هر تسک برای مستندسازی بهتر.</p>
            </div>
        
            <div class="p-6 bg-gradient-to-r from-gray-800 to-gray-600 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">پنل اختصاصی کاربران</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 12h18"/>
                  <path d="M3 6h18"/>
                  <path d="M3 18h18"/>
                </svg>
              </div>
              <p class="text-sm">پنل مدیریت مخصوص مدیران و پنل کاری جدا برای کاربران عادی با سطح دسترسی متفاوت.</p>
            </div>
        
            <div class="p-6 bg-gradient-to-r from-blue-800 to-cyan-600 rounded-2xl shadow-xl text-white">
              <div class="flex items-center gap-3 mb-2  justify-end flex-row-reverse
">
                <h2 class="text-xl font-bold">رتبه‌بندی و میتینگ</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 20h9"/>
                  <path d="M12 4h9"/>
                  <path d="M12 12h9"/>
                  <path d="M3 7a4 4 0 0 1 4-4h1"/>
                  <path d="M3 17a4 4 0 0 0 4 4h1"/>
                  <circle cx="6.5" cy="12" r="2.5"/>
                </svg>
              </div>
              <p class="text-sm">رتبه‌بندی کاربران بر اساس امتیاز و تعداد تسک‌های انجام‌شده، برگزاری جلسات پروژه.</p>
            </div>
        
          </div>
        </section>
      </main>
</template>

<script stup>
import { RouterLink } from 'vue-router';


</script>