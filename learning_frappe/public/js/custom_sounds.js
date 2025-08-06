const original_play_sound = frappe.utils.play_sound;
 
frappe.utils.play_sound = function (sound) {
    if (sound === 'delete') {
        console.log("🔊 Playing custom delete sound...");
        const audio = new Audio('/assets/learning_frappe/sounds/custom_delete.mp3');
        audio.play();
    } else {
        console.log(`Skipping sound: ${sound}`);
    }
};