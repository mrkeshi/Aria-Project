<template>
    <div class="max-w-sm w-full bg-white rounded-lg shadow dark:bg-gray-800 p-4 h-full ">
  
  <div class="flex justify-between mb-3">
      <div class="flex justify-center items-center">
          <div class="relative  flex flex-col gap-4 overflow-hidden rounded-none bg-transparent bg-clip-border text-gray-700 shadow-none md:flex-row md:items-center">
              <div class="w-max rounded-lg bg-purple-500 p-5 text-white">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3v11.25A2.25 2.25 0 0 0 6 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0 1 18 16.5h-2.25m-7.5 0h7.5m-7.5 0-1 3m8.5-3 1 3m0 0 .5 1.5m-.5-1.5h-9.5m0 0-.5 1.5M9 11.25v1.5M12 9v3.75m3-6v6" />
                    </svg>
                    
              </div>
              <div>
                <h6 class="block font-sans text-base font-semibold leading-relaxed tracking-normal text-purple-600 antialiased">
               دسته بندی تسک ها
                </h6>
                <p class="block max-w-sm font-sans text-sm font-normal leading-normal text-gray-700 antialiased">
               
                </p>
              </div>
            </div>
      
        </div>
   
  </div>



  <!-- Donut Chart -->
  <div class="py-6 md:pb-8" id="donut-chart"></div>


</div>
</template>

<script setup>
import { getCategory } from '@/services/ReportService';
import { useAuthStore } from '@/stores/auth';
import { onMounted, ref } from 'vue';

const user = useAuthStore();
const obd = ref([]);

onMounted(async () => {
  try {
    const res = await getCategory(user.user.access);
    res.data.forEach(task => {
      if (
        task.skill_name !== null &&
        task.skill_name !== undefined &&
        task.skill_name !== '' &&
        task.task_count !== null &&
        task.task_count !== undefined
      ) {
        obd.value.push({
          label: task.skill_name.toString(),
          count: Number(task.task_count)
        });
      }
    });

    if (obd.value.length === 0) {
      obd.value.push({ label: "ندارد", count: 0 });
    }

    const getChartOptions2 = () => {
      return {
        series: obd.value.map(item => item.count),
        colors: ["#30DD59", "#2889DB", "#DB4F18", "#FFE85C", "#FDBA8C", "#E74694", "#189F52", "#114893", "#30DD59", "#3366FF", "#930F2A"],
        chart: {
          height: 320,
          width: "100%",
          type: "donut",
        },
        stroke: {
          colors: ["transparent"],
        },
        plotOptions: {
          pie: {
            donut: {
              labels: {
                show: true,
                name: {
                  show: true,
                  fontFamily: "Inter, sans-serif",
                  offsetY: 20,
                },
                total: {
                  showAlways: true,
                  show: true,
                  label: "تعداد کل",
                  fontFamily: "Inter, sans-serif",
                  formatter: function (w) {
                    const sum = w.globals.seriesTotals.reduce((a, b) => a + b, 0);
                    return '' + sum + '';
                  },
                },
                value: {
                  show: true,
                  fontFamily: "Inter, sans-serif",
                  offsetY: -20,
                  formatter: function (value) {
                    return value + "";
                  },
                },
              },
              size: "80%",
            },
          },
        },
        grid: {
          padding: {
            top: -2,
          },
        },
        labels: obd.value.map(item => item.label),
        dataLabels: {
          enabled: false,
        },
        legend: {
          position: "bottom",
          fontFamily: "IRANYekanX, sans-serif",
        },
        yaxis: {
          labels: {
            formatter: function (value) {
              return value + "";
            },
          },
        },
        xaxis: {
          labels: {
            formatter: function (value) {
              return value + "";
            },
          },
          axisTicks: {
            show: false,
          },
          axisBorder: {
            show: false,
          },
        },
      };
    };

    if (document.getElementById("donut-chart") && typeof ApexCharts !== 'undefined') {
      const chart = new ApexCharts(document.getElementById("donut-chart"), getChartOptions2());
      chart.render();

      const checkboxes = document.querySelectorAll('#devices input[type="checkbox"]');
      function handleCheckboxChange(event, chart) {
        const checkbox = event.target;
        if (checkbox.checked) {
          switch (checkbox.value) {
            case 'desktop':
              chart.updateSeries([15.1, 22.5, 4.4, 8.4]);
              break;
            case 'tablet':
              chart.updateSeries([25.1, 26.5, 1.4, 3.4]);
              break;
            case 'mobile':
              chart.updateSeries([45.1, 27.5, 8.4, 2.4]);
              break;
            default:
              chart.updateSeries([55.1, 28.5, 1.4, 5.4]);
          }
        } else {
          chart.updateSeries([35.1, 23.5, 2.4, 5.4]);
        }
      }

      checkboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', (event) => handleCheckboxChange(event, chart));
      });
    }
  } catch (error) {
    console.error("خطا در دریافت داده‌ها:", error);
  }
});
</script>

<style>

</style>