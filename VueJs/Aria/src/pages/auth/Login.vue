<template>
  <div class="row">
        <section class="bg-white dark:bg-gray-900">
            <div class="container flex items-center justify-center min-h-screen px-6 mx-auto">
                <form class="w-full max-w-md" @submit.prevent="loginEvent">
              
        
                    <h1 class="mt-3 text-2xl font-semibold text-gray-800 capitalize sm:text-3xl dark:text-white">فرم ورود</h1>
        
                    <div class="relative flex items-center mt-8">
                        <span class="absolute">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 mx-3 text-gray-300 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                            </svg>
                        </span>
        
                        <input required v-model="user.email" type="text" class="block w-full py-3 text-gray-700 bg-white border rounded-lg px-11 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40" placeholder="آدرس ایمیل شما">
                    </div>
                    <RouterLink :to="{name:'forgot'}" class="inline-block mt-4 text-sm text-gray-500 capitalize hover:underline dark:text-blue-400">
                            رمز عبور فراموش کردی؟
                    </RouterLink>
                    <div class="relative flex items-center mt-4">
                        <span class="absolute">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 mx-3 text-gray-300 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                            </svg>
                        </span>
        
                        <input v-model="user.password" required type="password" class="block w-full px-10 py-3 text-gray-700 bg-white border rounded-lg dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40" placeholder="پسورد شما">
                    </div>
        
                    <div class="mt-6">
                        <button :class="[
                                'flex items-center submit justify-center bg-blue-500 hover:bg-blue-400 justify-between w-full px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                                loading ? ' disabled' : ''
                            ]" :disabled="loading">
                            ورود 
                        </button>
        
                       
        
                        <div class="mt-6 text-center ">
                            <RouterLink :to="{name:'register'}" class="text-sm text-blue-500 hover:underline dark:text-blue-400">
                                هنوز ثبت نام نکردی؟ کلیک کن
                            </RouterLink>
                        </div>
                    </div>
                </form>
            </div>
        </section>
    </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { RouterLink } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
const User=useAuthStore()
import { useToast } from "vue-toastification";
const loading = ref(false)
const toast = useToast();
const user = reactive({
    email: '',
    password: '',

});

const loginEvent = async () => {
    if (!loading.value) {
        loading.value=true
        await User.loginActions(user.email,user.password)
        loading.value=false
   
    }

}
</script>

<style>
</style>