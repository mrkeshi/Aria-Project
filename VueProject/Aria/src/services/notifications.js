import axios from "@/utils/axios";

export const saveOneSignalUserId = async (userId, token) => {
  const response = await axios.post(
    "noti/save-onesignal-userid/",
    { userId },
    {
      headers: {
        Authorization: `JWT ${token}`,
      },
    }
  );
  return response.data;
};
