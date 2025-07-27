export default function humanReadableTimeAgo(timestamp) {
    const now = new Date();
    const date = new Date(timestamp);
    const deltaSeconds = Math.floor((now - date) / 1000);

    if (deltaSeconds < 60) {
        return deltaSeconds <= 1 ? "یک لحظه قبل" : `${deltaSeconds} ثانیه قبل`;
    }

    const deltaMinutes = Math.floor(deltaSeconds / 60);
    if (deltaMinutes < 60) {
        return deltaMinutes === 1 ? "یک دقیقه قبل" : `${deltaMinutes} دقیقه قبل`;
    }

    const deltaHours = Math.floor(deltaMinutes / 60);
    if (deltaHours < 24) {
        return deltaHours === 1 ? "یک ساعت قبل" : `${deltaHours} ساعت قبل`;
    }

    const deltaDays = Math.floor(deltaHours / 24);
    if (deltaDays < 7) {
        return deltaDays === 1 ? "یک روز قبل" : `${deltaDays} روز قبل`;
    }

    const deltaWeeks = Math.floor(deltaDays / 7);
    if (deltaWeeks < 4) {
        return deltaWeeks === 1 ? "یک هفته قبل" : `${deltaWeeks} هفته قبل`;
    }

    const deltaMonths = Math.floor(deltaDays / 30);
    if (deltaMonths < 12) {
        return deltaMonths === 1 ? "یک ماه قبل" : `${deltaMonths} ماه قبل`;
    }

    const deltaYears = Math.floor(deltaDays / 365);
    return deltaYears === 1 ? "یک سال قبل" : `${deltaYears} سال قبل`;
}
