<template>
    <div class="row">
        <section class="bg-white dark:bg-gray-900">
            <div class="container flex items-center justify-center min-h-screen px-6 mx-auto">
                <form @submit.prevent="Resetevent" class="w-full max-w-md">


                    <h1 class="mt-3 text-2xl font-semibold text-gray-800 capitalize sm:text-3xl dark:text-white">تنظیم
                        مجدد رمز عبور</h1>

                    <div class="relative flex items-center mt-8">
                        <span class="absolute">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="w-6 h-6 mx-3 text-gray-300 dark:text-gray-500" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                            </svg>
                        </span>

                        <input v-model="user.password" required type="password"
                            class="block w-full px-10 py-3 text-gray-700 bg-white border rounded-lg dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40"
                            placeholder="پسورد">
                    </div>

                    <div class="relative flex items-center mt-4">
                        <span class="absolute">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="w-6 h-6 mx-3 text-gray-300 dark:text-gray-500" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                            </svg>
                        </span>

                        <input v-model="user.confirmpassword" required type="password"
                            class="block w-full px-10 py-3 text-gray-700 bg-white border rounded-lg dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40"
                            placeholder="تکرار پسورد">
                    </div>

                    <div class="mt-6">
                        <button :class="[
                            'flex items-center submit justify-center bg-blue-500 hover:bg-blue-400 justify-between w-full px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                            loading ? ' disabled' : ''
                        ]" :disabled="loading">
                            ذخیره
                        </button>

                    </div>
                </form>
            </div>
        </section>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { reactive, ref } from 'vue'
import { useToast } from 'vue-toastification'
import { useRoute,useRouter } from 'vue-router';
import { reset_password } from '@/services/auth';
const route = useRoute()
const router = useRouter()

const toast = useToast()
const loading = ref(false)
const user = reactive({
    password: '',
    confirmpassword: '',

})
const Resetevent = async () => {
    loading.value=true
    if (user.password !== user.confirmpassword) {
        toast.error("مقدار پسورد و تکرار پسورد باهم برابر نیست لطفا دقت فرمایید.")
    } else {
        let token = route.params.token
        let uid = route.params.uid
        await reset_password(uid, token, user.password).then((response) => {
            toast.success("رمز عبور شما با موفقیت تغییر یافت")
            router.push('/login')
        }).catch((error) => {
            let errordata = error.response.data
            console.log(errordata)
            Object.entries(errordata).forEach(([key, messages]) => {
                toast.error(`${messages}`);

            })
        }).finally(()=>{
            loading.value=false
            
        })
    }
}
</script>

<style></style>