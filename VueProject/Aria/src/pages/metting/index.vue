<template>

<div>

    <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8 px-4 ">
                <h1 class="text-gray-700 font-bold text-xl" >صفحه میتینگ</h1>
                <p class="text-gray-600 text-sm text-wrap">شما در این قسمت میتوانید از میتینگ استفاده کنید.</p>
             
                <div class="flex w-full flex-wrap max-md:justify-center justify-end mx-2 mt-6 ">
              
                
                </div>    
            </div>
           

            <section class=" w-full px-4 mx-auto ">
               <div class="flex flex-col justify-center items-center h-auto">
                    <RouterLink :to="{name:'video'}"class="bg-blue-500 w-96 h-16 hover:opacity-80 mb-8 font-IRANYekanX text-[28px] shadow-md flex rounded-md justify-center items-center text-white font-bold">تعریف نشست جدید</RouterLink>
                    <RouterLink :to="{name:'join'}" href="#" class="bg-blue-500 w-96 h-16 hover:opacity-70 mb-8 font-IRANYekanX text-[28px] shadow-md flex rounded-md justify-center items-center text-white font-bold">پیوستن به نشست </RouterLink>

                </div>
            </section>
</div>
</template>


<script setup>
import { RouterLink } from 'vue-router';


</script>

<style>

</style>