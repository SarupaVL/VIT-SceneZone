chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    const startDate = new Date(request.startDate);
    const endDate = new Date(request.endDate);
    endDate.setHours(23, 59, 59); // Include messages till the end of the day

    let messages = [];
    let messageCount = 0;

    const scrollUp = () => {
        window.scrollTo(0, 0); // Scroll to the top to load older messages
        setTimeout(() => extractMessages(), 1000);
    };

    const extractMessages = () => {
        const elements = document.querySelectorAll('div.message-in, div.message-out');

        elements.forEach(el => {
            const timeElement = el.querySelector('div.copyable-text');
            const textElement = el.querySelector('span.selectable-text');

            if (timeElement && textElement) {
                const timeText = timeElement.getAttribute('data-pre-plain-text');
                const textContent = textElement.textContent;

                const match = timeText.match(/\[\d{2}:\d{2}, (\d{1,2})\/(\d{1,2})\/(\d{4})\]/);
                if (match) {
                    const messageDate = new Date(`${match[3]}-${match[2]}-${match[1]}`);

                    if (messageDate >= startDate && messageDate <= endDate) {
                        messages.push(`${timeText} ${textContent}`);
                        messageCount++;
                        chrome.runtime.sendMessage({ count: messageCount, messages });
                    }
                }
            }
        });

        const oldestMessageDate = getOldestMessageDate(elements);
        if (oldestMessageDate > startDate) {
            scrollUp();
        }
    };

    const getOldestMessageDate = (elements) => {
        let oldestDate = new Date();
        elements.forEach(el => {
            const timeElement = el.querySelector('div.copyable-text');
            if (timeElement) {
                const timeText = timeElement.getAttribute('data-pre-plain-text');
                const match = timeText.match(/\[\d{2}:\d{2}, (\d{1,2})\/(\d{1,2})\/(\d{4})\]/);
                if (match) {
                    const messageDate = new Date(`${match[3]}-${match[2]}-${match[1]}`);
                    if (messageDate < oldestDate) {
                        oldestDate = messageDate;
                    }
                }
            }
        });
        return oldestDate;
    };

    extractMessages();
});
