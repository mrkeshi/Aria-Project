import Swal from 'sweetalert2';

export default function swalDel(){
return Swal.fire({
  title: "آیا برای حذف آن اطمینان دارید؟",
  text: "شما قادر به بازیابی آن نخواهید بود",
  icon: "error",
  showCancelButton: true,
  confirmButtonColor: "#ef4444",
  cancelButtonColor: "#2563eb",
  confirmButtonText: "بله، انجامش بده",
  cancelButtonText:"لغو"
})
}