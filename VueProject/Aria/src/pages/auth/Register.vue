<template>
    <div class="row">
        <section class="bg-white dark:bg-gray-900">
            <div class="flex justify-center min-h-screen">
                <div class="hidden bg-cover lg:block lg:w-2/5"
                    style="background-image: url('../../../public/assets/media/photo-1494621930069-4fd4b2e24a11.avif')">
                </div>

                <div class="flex items-center w-full max-w-3xl p-8 mx-auto lg:px-12 lg:w-3/5">
                    <div class="w-full">
                        <h1 class="text-2xl font-semibold  text-gray-800 capitalize dark:text-white">
                            به وب اپلیکیشن مدیریت پروژه خوش آمدید
                        </h1>






                        <form @submit.prevent="registerEvent" class="grid grid-cols-1 gap-6 mt-8 md:grid-cols-2">
                            <div>
                                <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">نام</label>
                                <input required type="text" v-model="user.firstname" placeholder="نام شما"
                                    class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                            </div>

                            <div>
                                <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">نام خانوادگی</label>
                                <input required type="text" v-model="user.lastname" placeholder="نام خانوادگی شما"
                                    class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                            </div>

                            <div>
                                <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">شماره تلفن</label>
                                <input required type="text" v-model="user.phone" placeholder="0990-788-1747"
                                    class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                            </div>

                            <div>
                                <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">آدرس ایمیل</label>
                                <input type="email" v-model="user.email" placeholder="johnsnow@example.com"
                                    class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40"
                                    required />
                            </div>

                            <div>
                                <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">پسورد</label>
                                <input type="password" v-model="user.password" placeholder="لطفا پسوردتان وارد کنید"
                                    class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40"
                                    required />
                            </div>

                            <div>
                                <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">تکرار پسورد</label>
                                <input type="password" v-model="user.confirmpassword"
                                    placeholder="پسوردتان را دوباره تکرار کنید"
                                    class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40"
                                    required />
                            </div>

                            <button :class="[
                                'flex items-center submit bg-blue-500 hover:bg-blue-400 justify-between w-full px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                                loading ? ' disabled' : ''
                            ]" :disabled="loading">
                                <span>ثبت نام</span>

                                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 rtl:-scale-x-100"
                                    viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd"
                                        d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                        clip-rule="evenodd" />
                                </svg>
                            </button>
                            <div class="mt-6 text-center  ">
                                <RouterLink :to="{ name: 'login' }"
                                    class="text-sm text-blue-500 hover:underline dark:text-blue-400">
                                    ثبت نام کردی؟ پس وارد شو.
                                </RouterLink>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    </div>

</template>

<script setup>
import { reactive, ref } from 'vue'
import { RouterLink } from 'vue-router';
import { register } from '@/services/auth';
import { useToast } from "vue-toastification";
import router from '@/router';
const loading = ref(false)
const toast = useToast();
const user = reactive({
    firstname: '',
    lastname: '',
    email: '',
    phone: null,
    password: '',
    confirmpassword: null,
});
function addCountryCode(phoneNumber) {
    if (phoneNumber.startsWith("0")) {
        return "+98" + phoneNumber.slice(1);
    } 
    else if (!phoneNumber.startsWith("+98")) {
        return "+98" + phoneNumber;
    }
    return phoneNumber;
}
const registerEvent = async () => {

    if (!loading.value) {
        user.phone=addCountryCode(user.phone)
        loading.value = true
       await register(user)
            .then(response => {
                loading.value = false
                console.log("User registered successfully:", response.data);
                toast.success("ثبت نام با موفقیت انجام شد لطفا اقدام به فعالسازی اکانت نمایید.")
                router.push("/login")
            })
            .catch(error => {
                console.log(error)
                let errordata=error.response.data 
                console.log(errordata)
                Object.entries(errordata).forEach(([key, messages]) => {
    
                    toast.error(`${messages}`);

                })
            }).finally(() => {
                loading.value = false

            });
   
    }

}
</script>


<style></style>