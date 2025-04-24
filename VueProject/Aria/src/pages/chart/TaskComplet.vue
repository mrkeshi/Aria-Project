<template>
      <div class="relative flex flex-col rounded-xl bg-white bg-clip-border text-gray-700 shadow">
                            <div class="relative mx-4 mt-4 flex flex-col gap-4 overflow-hidden rounded-none bg-transparent bg-clip-border text-gray-700 shadow-none md:flex-row md:items-center">
                              <div class="w-max rounded-lg bg-gray-900 p-5 text-white">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3v11.25A2.25 2.25 0 0 0 6 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0 1 18 16.5h-2.25m-7.5 0h7.5m-7.5 0-1 3m8.5-3 1 3m0 0 .5 1.5m-.5-1.5h-9.5m0 0-.5 1.5m.75-9 3-3 2.148 2.148A12.061 12.061 0 0 1 16.5 7.605" />
                                  </svg>
                                  
                              </div>
                              <div>
                                <h6 class="block font-sans text-base font-semibold leading-relaxed tracking-normal text-blue-gray-900 antialiased">
                                  آمار تسک های انجام شده (ده روز قبل)
                                </h6>
                                <p class="block max-w-sm font-sans text-sm font-normal leading-normal text-gray-700 antialiased">
                               
                                </p>
                              </div>
                            </div>
                            <div  class="pt-6 px-2 pb-0">
                              <div id="bar-chart"></div>
                            </div>
                          </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useReportStore } from '@/stores/Reporting';
const auth=useAuthStore()
const report=useReportStore()

onMounted(async()=>{
    
await report.getTaskAgo(auth.user.access)

const chartConfig = {
  series: [
    {
      name: "انجام شده",
      data: report.task.map(item => item.count),
    },
  ],
  chart: {
    type: "bar",
    height: 240,
    toolbar: {
      show: true,
    },
  },
  title: {
    show: "",
  },
  dataLabels: {
    enabled: false,
  },
  colors: ["#020617"],
  plotOptions: {
    bar: {
      columnWidth: "40%",
      borderRadius: 2,
    },
  },
  xaxis: {
    axisTicks: {
      show: false,
    },
    axisBorder: {
      show: false,
    },
    labels: {
      style: {
        colors: "#616161",
        fontSize: "12px",
        fontFamily: "inherit",
        fontWeight: 400,
      },
    },
    categories: report.task.map(item => item.date),
  },
  yaxis: {
    labels: {
      style: {
        colors: "#616161",
        fontSize: "12px",
        fontFamily: "inherit",
        fontWeight: 400,
      },
    },
  },
  grid: {
    show: true,
    borderColor: "#dddddd",
    strokeDashArray: 5,
    xaxis: {
      lines: {
        show: true,
      },
    },
    padding: {
      top: 5,
      right: 20,
    },
  },
  fill: {
    opacity: 0.8,
  },
  tooltip: {
    theme: "dark",
  },
};
 
  const chart = new ApexCharts(document.querySelector("#bar-chart"), chartConfig);
  
  chart.render();

})

</script>

<style>
</style>