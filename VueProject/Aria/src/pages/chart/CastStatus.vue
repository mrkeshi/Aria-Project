<template>
   <div class="max-w-sm w-full bg-white rounded-lg shadow dark:bg-gray-800 md:p-4">
                            <div class="flex justify-between mb-3">
                              <div class="flex items-center">
                                <div class="flex justify-center items-center">
                                    <div class="relative  flex flex-col gap-4 overflow-hidden rounded-none bg-transparent bg-clip-border text-gray-700 shadow-none md:flex-row md:items-center">
                                        <div class="w-max rounded-lg bg-green-400 p-5 text-white">
                                          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" class="h-6 w-6">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M6.429 9.75L2.25 12l4.179 2.25m0-4.5l5.571 3 5.571-3m-11.142 0L2.25 7.5 12 2.25l9.75 5.25-4.179 2.25m0 0L21.75 12l-4.179 2.25m0 0l4.179 2.25L12 21.75 2.25 16.5l4.179-2.25m11.142 0l-5.571 3-5.571-3"></path>
                                          </svg>
                                        </div>
                                        <div>
                                          <h6 class="block font-sans text-base font-semibold leading-relaxed tracking-normal text-green-500 antialiased">
                                           وضعیت تسک ها
                                          </h6>
                                          <p class="block max-w-sm font-sans text-sm font-normal leading-normal text-gray-700 antialiased">
                                         
                                          </p>
                                        </div>
                                      </div>
                              
                         
                                </div>
                              </div>
                            </div>
                          
                            <div class="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg">
                              <div class="grid grid-cols-3 gap-3 mb-2">
                                <dl class="bg-orange-50 dark:bg-gray-600 rounded-lg flex flex-col items-center justify-center h-[78px]">
                                  <dt class="w-8 h-8 rounded-full bg-orange-100 dark:bg-gray-500 text-orange-600 dark:text-orange-300 text-sm font-medium flex items-center justify-center mb-1">{{myobj.dontworking}}</dt>
                                  <dd class="text-orange-600 dark:text-orange-300 text-sm font-medium">برای انجام دادن</dd>
                                </dl>
                                <dl class="bg-teal-50 dark:bg-gray-600 rounded-lg flex flex-col items-center justify-center h-[78px]">
                                  <dt class="w-8 h-8 rounded-full bg-teal-100 dark:bg-gray-500 text-teal-600 dark:text-teal-300 text-sm font-medium flex items-center justify-center mb-1">{{myobj.working}}</dt>
                                  <dd class="text-teal-600 dark:text-teal-300 text-sm font-medium">در حال انجام </dd>
                                </dl>
                                <dl class="bg-blue-50 dark:bg-gray-600 rounded-lg flex flex-col items-center justify-center h-[78px]">
                                  <dt class="w-8 h-8 rounded-full bg-blue-100 dark:bg-gray-500 text-blue-600 dark:text-blue-300 text-sm font-medium flex items-center justify-center mb-1">{{myobj.done}}</dt>
                                  <dd class="text-blue-600 dark:text-blue-300 text-sm font-medium">تکمیل شده</dd>
                                </dl>
                              </div>
                   
                            
                            </div>
                          
                            <!-- Radial Chart -->
                            <div class="py-2" id="radial-chart"></div>
                          
                          </div>
</template>

<script setup>
import { getTaskStatus } from '@/services/ReportService';
import { useAuthStore } from '@/stores/auth';
import { onMounted, ref } from 'vue';
const auth=useAuthStore()
const myobj=ref({
  done:0,
  working:0,
  dontworking:0
})
onMounted(async()=>{
 await getTaskStatus(auth.user.access).then((res)=>{
    res.data.forEach(task => {
  if ( task.progress === 0) {
    myobj.value.dontworking += 1; 
  } else if ( task.progress === 100) {
    myobj.value.done += 1; 
  } else {
    myobj.value.working += 1; 
  }
});
  })
  const total=myobj.value.dontworking+myobj.value.done+myobj.value.working

    const getChartOptions = () => {
  return {
    
    series: [(myobj.value.done/total)*100,(myobj.value.working/total)*100,(myobj.value.dontworking/total)*100],
    colors: ["#1C64F2", "#16BDCA", "#FDBA8C"],
    chart: {
      height: "300px",
      width: "100%",
      type: "radialBar",
      sparkline: {
        enabled: true,
      },
    },
    plotOptions: {
      radialBar: {
        track: {
          background: '#E5E7EB',
        },
        dataLabels: {
          show: false,
        },
        hollow: {
          margin: 0,
          size: "32%",
        }
      },
    },
    grid: {
      show: false,
      strokeDashArray: 4,
      padding: {
        left: 2,
        right: 2,
        top: -23,
        bottom: -20,
      },
    },
    labels: ["تکمیل شده", "در حال جریان", "برای انجام دادن"],
    legend: {
      show: true,
      position: "bottom",
      fontFamily: "Inter, sans-serif",
    },
    tooltip: {
      enabled: true,
      x: {
        show: false,
      },
    },
    yaxis: {
      show: false,
      labels: {
        formatter: function (value) {
          return value + '%';
        }
      }
    }
  }
}

if (document.getElementById("radial-chart") && typeof ApexCharts !== 'undefined') {
  const chart = new ApexCharts(document.querySelector("#radial-chart"), getChartOptions());
  chart.render();
}
})
</script>

<style>

</style>