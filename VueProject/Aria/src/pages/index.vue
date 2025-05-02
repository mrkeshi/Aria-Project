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
                <p class="mx-1 font-semibold">شروع کنید</p>
              </button>
            </div>
            <div class="mt-8 lg:w-1/2 lg:px-4 lg:mt-0">
              <img class="object-cover w-full rounded-xl h-96" src="https://images.unsplash.com/photo-1516131206008-dd041a9764fd?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=880&amp;q=80" alt="Video thumbnail">
            </div>
          </div>
        </section>
      
        <section class="container px-6 py-8 mx-auto lg:py-16">
          <div class="grid grid-cols-1 gap-8 xl:gap-12 md:grid-cols-2 xl:grid-cols-3">
            <div class="p-8 space-y-3 border-2 border-indigo-400 rounded-xl">
              <span class="inline-block text-indigo-500">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.879 16.121A3 3 0 1012.015 11L11 14H9c0 .768.293 1.536.879 2.121z"></path>
                </svg>
              </span>
              <h1 class="text-2xl font-semibold text-gray-700 capitalize text-right">مدیریت تسک‌ها</h1>
              <p class="text-gray-500">تعریف، مدیریت و پیگیری تسک‌ها با درصد پیشرفت پروژه و زمان‌بندی دقیق</p>
            </div>
            <div class="p-8 space-y-3 border-2 border-indigo-400 rounded-xl">
              <span class="inline-block text-indigo-500">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z"></path>
                </svg>
              </span>
              <h1 class="text-2xl font-semibold text-gray-700 capitalize text-right">ارتباط تیمی</h1>
              <p class="text-gray-500">سیستم گفت‌و‌گوی داخل برنامه برای ارتباط میان اعضای تیم و مدیران</p>
            </div>
            <div class="p-8 space-y-3 border-2 border-indigo-400 rounded-xl">
              <span class="inline-block text-indigo-500">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path>
                </svg>
              </span>
              <h1 class="text-2xl font-semibold text-gray-700 capitalize text-right">گزارش‌ها</h1>
              <p class="text-gray-500">گزارش‌های دقیق از پیشرفت پروژه و وضعیت تسک‌ها به صورت نمودار و گزارش‌های فیلتر شده</p>
            </div>
          </div>
        </section>
      </main>
</template>

<script stup>
import { RouterLink } from 'vue-router';


</script>