#define CAMERA_MODEL_AI_THINKER
#include "esp_camera.h"

// ====== AI THINKER PIN CONFIG ======
void initCamera() {
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = 5;
  config.pin_d1 = 18;
  config.pin_d2 = 19;
  config.pin_d3 = 21;
  config.pin_d4 = 36;
  config.pin_d5 = 39;
  config.pin_d6 = 34;
  config.pin_d7 = 35;
  config.pin_xclk = 0;
  config.pin_pclk = 22;
  config.pin_vsync = 25;
  config.pin_href = 23;
  config.pin_sscb_sda = 26;
  config.pin_sscb_scl = 27;
  config.pin_pwdn = 32;
  config.pin_reset = -1;

  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;

  // Lower resolution = more stable over Serial
  config.frame_size = FRAMESIZE_QQVGA;

  config.jpeg_quality = 12;
  config.fb_count = 1;

  if (esp_camera_init(&config) != ESP_OK) {
    Serial.println("❌ Camera init failed");
    while (true);
  }

  Serial.println("✅ Camera initialized");
}

// ================================

void setup() {
  Serial.begin(921600);
  delay(2000);

  initCamera();
}

void loop() {

  camera_fb_t * fb = esp_camera_fb_get();

  if (!fb) {
    return;
  }

  uint32_t img_size = fb->len;

  // Send size first
  Serial.write((uint8_t*)&img_size, sizeof(img_size));

  // Send image
  Serial.write(fb->buf, fb->len);

  esp_camera_fb_return(fb);

  delay(3000);
}
