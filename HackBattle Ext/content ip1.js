chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    const startDate = new Date(request.startDate);
    const endDate = new Date(request.endDate);
    endDate.setHours(23, 59, 59); // Ensure messages up to the end of the day are included

    let messages = new Set();
    let messageCount = 0;

    const scrollInterval = 2000;  // Time interval between scroll attempts
    let lastScrollHeight = 0;     // To detect if more messages have loaded

    const scrollUpAndExtract = () => {
        const chat = document.querySelector("div[role='list']") || document.querySelector("div[data-testid='conversation-container']");  // Fallback to alternative selector
        if (chat) {
            chat.scrollTop = 0;  // Scroll to top to load older messages
            setTimeout(extractMessages, scrollInterval);
        } else {
            console.error("Message container not found. Please ensure you are in the correct chat.");
            sendResponse({ messages: Array.from(messages), count: messages.size }); // Send current messages and count
        }
    };

    const extractMessages = () => {
        const elements = document.querySelectorAll("div.copyable-text");
        elements.forEach(el => {
            const timeText = el.getAttribute('data-pre-plain-text');
            const textElement = el.querySelector("span.selectable-text");

            if (timeText && textElement) {
                // Extracting the date and time
                const messageDateString = timeText.match(/\[(.*?)\]/)[1]; // Extracts the timestamp inside the brackets
                const messageDate = new Date(messageDateString.replace(',', '')); // Convert to Date object

                // Check if the message date is within the specified range
                if (messageDate >= startDate && messageDate <= endDate) {
                    messages.add(textElement.innerText);
                    messageCount++;
                    console.log(`Extracted message: ${textElement.innerText}`);
                }
            }
        });

        if (messageCount === 0 || chat.scrollHeight === lastScrollHeight) {
            // Stop scrolling if no new messages or reached the end
            console.log(`Finished extracting messages. Total: ${messages.size}`);
            sendResponse({ messages: Array.from(messages), count: messages.size });
        } else {
            lastScrollHeight = chat.scrollHeight;
            scrollUpAndExtract();
        }
    };

    scrollUpAndExtract();
    return true; // Indicates that the response will be sent asynchronously
});
