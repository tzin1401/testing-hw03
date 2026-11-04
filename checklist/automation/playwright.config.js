const { defineConfig } = require('@playwright/test');
module.exports = defineConfig({
  testDir: __dirname, testMatch: 'run-chrome.spec.js', workers: 1, retries: 0,
  timeout: 90000, reporter: [['line'], ['json', {outputFile: require('path').resolve(process.env.PW_JSON_REPORT || require('path').join(__dirname,'playwright-results.json'))}]],
  outputDir: require('path').join(__dirname,'test-results'),
  use: {channel:'chrome', headless:false, viewport:{width:1280,height:800},
    baseURL:'http://localhost:5173', permissions:['clipboard-read','clipboard-write'],
    screenshot:'off', trace:'off', actionTimeout:6000, navigationTimeout:15000}
});
