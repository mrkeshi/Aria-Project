<template>

<div>

    <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8 px-4 ">
                <h1 class="text-gray-700 font-bold text-xl" >صفحه میتینگ</h1>
                <p class="text-gray-600 text-sm text-wrap">شما در این قسمت میتوانید از میتینگ استفاده کنید.</p>
             
                <div class="flex w-full flex-wrap max-md:justify-center justify-end mx-2 mt-6 ">
              
                
                </div>    
            </div>
           
          
            <section class=" w-full  mx-auto ">
               <div class="flex flex-col justify-center items-center h-auto">
                    <RouterLink :to="{name:'video'}" style="margin:10px 0px;padding: 15px;width: 100%;" class="bg-blue-500 w-96 h-16 hover:opacity-80 mb-8 font-IRANYekanX text-[28px] shadow-md flex rounded-md justify-center items-center text-white font-bold">تعریف نشست جدید</RouterLink>
                    <RouterLink :to="{name:'join'}" style="margin:10px 0px;padding: 15px;width: 100%;" href="#" class="bg-blue-500 w-96 h-16 hover:opacity-70 mb-8 font-IRANYekanX text-[28px] shadow-md flex rounded-md justify-center items-center text-white font-bold">پیوستن به نشست </RouterLink>

                </div>
            </section>
            <section class="w-full px- mx-auto" v-show="(!subStore.isActive || subStore.level<3)">

<div class="mx-auto my-12  px-6 py-8  text-blue-500 rounded-2xl  transition-all duration-300 hover:scale-[1.01]" dir="rtl" style="border:2px #3b82f6 solid ;">
<div class="flex items-center mb-6">
    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 mt-1 text-blue-500 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="margin:5px 5px;margin-top: -5px;">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01M10.29 3.86L1.82 18a1 1 0 00.86 1.5h18.64a1 1 0 00.86-1.5L13.71 3.86a1 1 0 00-1.72 0z" />
  </svg>
<h2 class="text-2xl font-extrabold tracking-tight">قابلیت طلایی فقط برای مدیران حرفه‌ای</h2>
</div>

<p class="text-sm leading-loose mb-6">
در این پروژه، قابلیتی ویژه تعریف شده است که فقط در صورتی برای کل اعضای پروژه فعال می‌شود که:
<br />
<strong>۱.</strong> شما مدیر پروژه باشید.
<strong>۲.</strong> اشتراک <span class="font-semibold underline decoration-white/70">طلایی</span> فعال داشته باشید.
در این صورت، این ویژگی برای تمام کاربران شما به‌صورت خودکار فعال می‌شود و آن‌ها می‌توانند از آن استفاده کنند.

اگر اشتراک طلایی نداشته باشید، این قابلیت در پروژه‌ی شما فعال نمی‌شود، حتی اگر مدیر باشید.
ولی اگر عضو پروژه‌ای باشید که مدیر آن اشتراک طلایی دارد و این ویژگی را فعال کرده، شما هم به‌عنوان کاربر عادی، می‌توانید از آن بهره ببرید.
</p>

<div class="text-center">
<RouterLink :to="{name:'sub'}"  class="inline-block bg-white text-blue-500 font-semibold px-5 py-3 rounded-full shadow-md  transition duration-300">
خرید اشتراک طلایی
</RouterLink>
</div>
</div>

</section>
</div>
</template>


<script setup>
import { useAuthStore } from '@/stores/auth';
import { useSubStore } from '@/stores/SubStore';
import { onMounted } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';
const toast=useToast()
const router=useRouter()
const subStore=useSubStore()

onMounted(async ()=>{
    await subStore.fetchSubscriptionStatus(useAuthStore().user.access);

    if( (subStore.manager_plan!="gold" || !subStore.manager_plan_active)){
        router.push({'name':'dashbaord'})
        toast.info("قابلیت کنفرانس ویدئویی توسط مدیر پروژه فعال نشده است.")
    }
})

</script>

<style>

</style>