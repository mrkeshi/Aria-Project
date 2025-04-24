<template>
<div>
  <BestUser></BestUser>
                <!-- chart -->
                <section>
                <div class="container px-6 py-10 mx-auto grid grid-cols-11 gap-4">
                    <div class="col-span-5 flex flex-col">
                  <TaskComplet></TaskComplet>
                   
                   
                   <div class="w-full mt-4">
             <ProgressSingleProject></ProgressSingleProject>
                   </div>
                        </div>

                    <div class="col-span-3">

                     
                        <CastStatus></CastStatus>
                        
                    </div>
                    <div class="col-span-3">
                          

                      <TaskCateGory></TaskCateGory>
                    </div>
                </div>
            </section>
</div>
</template>
<script setup>
import BestUser from '@/pages/chart/BestUser.vue'
import TaskCateGory from './chart/TaskCateGory.vue';
import CastStatus from './chart/CastStatus.vue';
import "@/assets/chart.css"
import { onMounted } from "vue";
import ProgressSingleProject from './chart/ProgressSingleProject.vue';
import TaskComplet from './chart/TaskComplet.vue';
onMounted(async ()=>{
 





})

</script>
<style>

</style>