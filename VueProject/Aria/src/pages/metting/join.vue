<template>

<div>

    <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8 px-4 ">
                <h1 class="text-gray-700 font-bold text-xl" >پیوستن </h1>
             
                <div class="flex w-full flex-wrap max-md:justify-center justify-end mx-2 mt-6 ">
              
                
                </div>    
            </div>
           

            <div style="width: 500px; height: 220px;justify-content: center; margin: 0 auto;" class="flex justify-center flex-col items-center bg-white rounded-md bg-white-500 shadow-md h-[220px] w-[500px] p-8 ">

<input v-model="ID" required type="text" class="block mb-6 w-full h-28 px-10 py-3  text-gray-700 bg-white border rounded-lg dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40" placeholder="آیدی نشست را وارد کنید. ">
<button @click="send()" class="w-full mb-4 text-xl  px-6 py-3 text-md font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-blue-500 rounded-lg hover:opacity-80 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50">
    ورود 
</button>
</div>
</div>
</template>


<script setup>
import { useAuthStore } from '@/stores/auth';
import { useSubStore } from '@/stores/SubStore';
import { ref,onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';
const toast=useToast()
const router=useRouter()
const subStore=useSubStore()

onMounted(async ()=>{
    await subStore.fetchSubscriptionStatus(useAuthStore().user.access);
    if((!subStore.isActive || subStore.level<3) && (subStore.manager_plan!="gold" || !subStore.manager_plan_active)){
        router.push({'name':'dashbaord'})
        toast.info("قابلیت کنفرانس ویدئویی توسط مدیر پروژه فعال نشده است.")
    }
})
const ID=ref()

const send=()=>{
    if(ID.value){
            
            return router.push("/videocal?roomID="+ID.value)
    }
}


</script>

<style>

</style>