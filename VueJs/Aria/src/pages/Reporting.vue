<template>
<div>
  <BestUser></BestUser>
                <!-- chart -->
                <section>
                <div id="" class="container grid_res_me px-6 py-10 mx-auto grid grid-cols-11 gap-4 custom-grid">
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
@media (max-width: 768px) {
    .custom-grid {
        grid-template-columns: 1fr; 
    }

    .custom-grid .col-span-5,
    .custom-grid .col-span-3 {
        grid-column: span 1 / span 1; 
    }
}
</style>