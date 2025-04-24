<template>
    <div class="row">
        <section class="bg-white dark:bg-gray-900">
            <div class="container flex items-center justify-center min-h-screen px-6 mx-auto">
                <form @submit.prevent="Resetevent" class="w-full max-w-md">
              
        
                    <h1 class="mt-3 text-2xl font-semibold text-gray-800 capitalize sm:text-3xl dark:text-white">فراموشی رمز عبور</h1>
                    <a href="#" class="inline-block mt-4 text-sm text-gray-500 capitalize hover:underline dark:text-blue-400">
                            جهت بازیابی رمز عبور، لطفا ایمیل خود را وارد کنید.
                    </a>
                    <div class="relative flex items-center mt-8">
                        <span class="absolute">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 mx-3 text-gray-300 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                            </svg>
                        </span>
        
                        <input v-model="email" required type="email" class="block w-full px-10 py-3 text-gray-700 bg-white border rounded-lg dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40" placeholder="ایمیل">
                    </div>
                
                    <div class="mt-6">
                        <button :class="[
                                'flex items-center submit justify-center bg-blue-500 hover:bg-blue-400 justify-between w-full px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                                loading ? ' disabled' : ''
                            ]" :disabled="loading">
                            بازیابی رمز عبور 
                        </button>
        
                    </div>
                </form>
            </div>
        </section>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import {  ref } from 'vue'
import { useToast } from 'vue-toastification';
const toast=useToast()
import { forgotpass } from '@/services/auth';
import router from '@/router';
const email=ref('')
const loading=ref(false)
function Resetevent(){
    if(!loading.value){
        loading.value=true
forgotpass(email.value).then((response)=>{
    toast.success("ایمیل حاوی رمز عبور برای شما با موفقیت ارسال شد")
    router.push('/login')

}).catch((err)=>{
    console.log(err)
    toast.error("لطفا ایمیل معتبر وارد کنید، ایمیل شما یافت نشد")
}).finally(()=>{
    email.value=""
    loading.value=false
})

    }
}
</script>

<style>

</style>