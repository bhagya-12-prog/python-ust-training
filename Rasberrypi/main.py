<!DOCTYPE html>
<!-- saved from url=(0053)https://wokwi.com/arduino/projects/325015245126894163 -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style data-emotion="css-global" data-s="">html{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;box-sizing:border-box;-webkit-text-size-adjust:100%;}*,*::before,*::after{box-sizing:inherit;}strong,b{font-weight:700;}body{margin:0;color:#fff;font-family:"Roboto","Helvetica","Arial",sans-serif;font-weight:400;font-size:1rem;line-height:1.5;letter-spacing:0.00938em;background-color:#121212;}@media print{body{background-color:#fff;}}body::backdrop{background-color:#121212;}</style><style data-emotion="css xxj4es nabnrl 1b0rp8j 6xugel vubbuv 1me3vhm n3zf6c 1l1swz3" data-s="">.css-xxj4es{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;position:relative;box-sizing:border-box;-webkit-tap-highlight-color:transparent;background-color:transparent;outline:0;border:0;margin:0;border-radius:0;padding:0;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;vertical-align:middle;-moz-appearance:none;-webkit-appearance:none;-webkit-text-decoration:none;text-decoration:none;color:inherit;font-family:"Roboto","Helvetica","Arial",sans-serif;font-weight:500;font-size:0.875rem;line-height:1.75;letter-spacing:0.02857em;text-transform:uppercase;min-width:64px;padding:6px 16px;border-radius:4px;-webkit-transition:background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;transition:background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;color:#fff;background-color:#9c27b0;box-shadow:0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12);}.css-xxj4es::-moz-focus-inner{border-style:none;}.css-xxj4es.Mui-disabled{pointer-events:none;cursor:default;}@media print{.css-xxj4es{-webkit-print-color-adjust:exact;color-adjust:exact;}}.css-xxj4es:hover{-webkit-text-decoration:none;text-decoration:none;background-color:rgb(109, 27, 123);box-shadow:0px 2px 4px -1px rgba(0,0,0,0.2),0px 4px 5px 0px rgba(0,0,0,0.14),0px 1px 10px 0px rgba(0,0,0,0.12);}@media (hover: none){.css-xxj4es:hover{background-color:#9c27b0;}}.css-xxj4es:active{box-shadow:0px 5px 5px -3px rgba(0,0,0,0.2),0px 8px 10px 1px rgba(0,0,0,0.14),0px 3px 14px 2px rgba(0,0,0,0.12);}.css-xxj4es.Mui-focusVisible{box-shadow:0px 3px 5px -1px rgba(0,0,0,0.2),0px 6px 10px 0px rgba(0,0,0,0.14),0px 1px 18px 0px rgba(0,0,0,0.12);}.css-xxj4es.Mui-disabled{color:rgba(255, 255, 255, 0.3);box-shadow:none;background-color:rgba(255, 255, 255, 0.12);}.css-nabnrl{text-align:center;font-size:20px;margin-top:32px;}.css-1b0rp8j{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;position:relative;box-sizing:border-box;-webkit-tap-highlight-color:transparent;background-color:transparent;outline:0;border:0;margin:0;border-radius:0;padding:0;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;vertical-align:middle;-moz-appearance:none;-webkit-appearance:none;-webkit-text-decoration:none;text-decoration:none;color:inherit;font-family:"Roboto","Helvetica","Arial",sans-serif;font-weight:500;font-size:0.875rem;line-height:1.75;letter-spacing:0.02857em;text-transform:uppercase;min-width:64px;padding:6px 16px;border-radius:4px;-webkit-transition:background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;transition:background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;color:#fff;background-color:#9c27b0;box-shadow:0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12);vertical-align:bottom;}.css-1b0rp8j::-moz-focus-inner{border-style:none;}.css-1b0rp8j.Mui-disabled{pointer-events:none;cursor:default;}@media print{.css-1b0rp8j{-webkit-print-color-adjust:exact;color-adjust:exact;}}.css-1b0rp8j:hover{-webkit-text-decoration:none;text-decoration:none;background-color:rgb(109, 27, 123);box-shadow:0px 2px 4px -1px rgba(0,0,0,0.2),0px 4px 5px 0px rgba(0,0,0,0.14),0px 1px 10px 0px rgba(0,0,0,0.12);}@media (hover: none){.css-1b0rp8j:hover{background-color:#9c27b0;}}.css-1b0rp8j:active{box-shadow:0px 5px 5px -3px rgba(0,0,0,0.2),0px 8px 10px 1px rgba(0,0,0,0.14),0px 3px 14px 2px rgba(0,0,0,0.12);}.css-1b0rp8j.Mui-focusVisible{box-shadow:0px 3px 5px -1px rgba(0,0,0,0.2),0px 6px 10px 0px rgba(0,0,0,0.14),0px 1px 18px 0px rgba(0,0,0,0.12);}.css-1b0rp8j.Mui-disabled{color:rgba(255, 255, 255, 0.3);box-shadow:none;background-color:rgba(255, 255, 255, 0.12);}.css-6xugel{display:inherit;margin-right:8px;margin-left:-4px;}.css-6xugel>*:nth-of-type(1){font-size:20px;}.css-vubbuv{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;width:1em;height:1em;display:inline-block;fill:currentColor;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;-webkit-transition:fill 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;transition:fill 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;font-size:1.5rem;}.css-1me3vhm{font-size:150%;font-family:var(--default-font);}.css-n3zf6c{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;position:relative;box-sizing:border-box;-webkit-tap-highlight-color:transparent;background-color:transparent;outline:0;border:0;margin:0;border-radius:0;padding:0;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;vertical-align:middle;-moz-appearance:none;-webkit-appearance:none;-webkit-text-decoration:none;text-decoration:none;color:inherit;font-family:"Roboto","Helvetica","Arial",sans-serif;font-weight:500;font-size:0.875rem;line-height:1.75;letter-spacing:0.02857em;text-transform:uppercase;min-width:64px;padding:6px 16px;border-radius:4px;-webkit-transition:background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;transition:background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;color:#fff;background-color:#9c27b0;box-shadow:0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12);margin-right:32px;}.css-n3zf6c::-moz-focus-inner{border-style:none;}.css-n3zf6c.Mui-disabled{pointer-events:none;cursor:default;}@media print{.css-n3zf6c{-webkit-print-color-adjust:exact;color-adjust:exact;}}.css-n3zf6c:hover{-webkit-text-decoration:none;text-decoration:none;background-color:rgb(109, 27, 123);box-shadow:0px 2px 4px -1px rgba(0,0,0,0.2),0px 4px 5px 0px rgba(0,0,0,0.14),0px 1px 10px 0px rgba(0,0,0,0.12);}@media (hover: none){.css-n3zf6c:hover{background-color:#9c27b0;}}.css-n3zf6c:active{box-shadow:0px 5px 5px -3px rgba(0,0,0,0.2),0px 8px 10px 1px rgba(0,0,0,0.14),0px 3px 14px 2px rgba(0,0,0,0.12);}.css-n3zf6c.Mui-focusVisible{box-shadow:0px 3px 5px -1px rgba(0,0,0,0.2),0px 6px 10px 0px rgba(0,0,0,0.14),0px 1px 18px 0px rgba(0,0,0,0.12);}.css-n3zf6c.Mui-disabled{color:rgba(255, 255, 255, 0.3);box-shadow:none;background-color:rgba(255, 255, 255, 0.12);}.css-1l1swz3{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;position:relative;box-sizing:border-box;-webkit-tap-highlight-color:transparent;background-color:transparent;outline:0;border:0;margin:0;border-radius:0;padding:0;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;vertical-align:middle;-moz-appearance:none;-webkit-appearance:none;-webkit-text-decoration:none;text-decoration:none;color:inherit;font-family:"Roboto","Helvetica","Arial",sans-serif;font-weight:500;font-size:0.875rem;line-height:1.75;letter-spacing:0.02857em;text-transform:uppercase;min-width:64px;padding:6px 16px;border-radius:4px;-webkit-transition:background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;transition:background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;color:rgba(0, 0, 0, 0.87);background-color:#66bb6a;box-shadow:0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12);}.css-1l1swz3::-moz-focus-inner{border-style:none;}.css-1l1swz3.Mui-disabled{pointer-events:none;cursor:default;}@media print{.css-1l1swz3{-webkit-print-color-adjust:exact;color-adjust:exact;}}.css-1l1swz3:hover{-webkit-text-decoration:none;text-decoration:none;background-color:#388e3c;box-shadow:0px 2px 4px -1px rgba(0,0,0,0.2),0px 4px 5px 0px rgba(0,0,0,0.14),0px 1px 10px 0px rgba(0,0,0,0.12);}@media (hover: none){.css-1l1swz3:hover{background-color:#66bb6a;}}.css-1l1swz3:active{box-shadow:0px 5px 5px -3px rgba(0,0,0,0.2),0px 8px 10px 1px rgba(0,0,0,0.14),0px 3px 14px 2px rgba(0,0,0,0.12);}.css-1l1swz3.Mui-focusVisible{box-shadow:0px 3px 5px -1px rgba(0,0,0,0.2),0px 6px 10px 0px rgba(0,0,0,0.14),0px 1px 18px 0px rgba(0,0,0,0.12);}.css-1l1swz3.Mui-disabled{color:rgba(255, 255, 255, 0.3);box-shadow:none;background-color:rgba(255, 255, 255, 0.12);}</style><style data-emotion="css" data-s=""></style><meta name="viewport" content="width=device-width"><title class="jsx-2817566372">sketch.ino - Wokwi Arduino and ESP32 Simulator</title><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@WokwiMakes"><link rel="alternate" type="application/json+oembed" href="https://wokwi.com/api/oembed?url=https%3A%2F%2Fwokwi.com%2Fshare%2F325015245126894163" title="Wokwi oEmbed provider" class="jsx-4253649316"><meta property="og:title" content="sketch.ino - Wokwi Arduino and ESP32 Simulator"><meta property="og:description" content="Run Arduino projects in your browser, no installation required!"><meta property="og:image" content="https://thumbs.wokwi.com/projects/325015245126894163/social/1646217541630.png"><meta name="next-head-count" content="12"><meta name="theme-color" content="#9c27b0"><link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin=""><link rel="preload" href="./main_files/1cf64f00f4a3096f.css" as="style"><link rel="stylesheet" href="./main_files/1cf64f00f4a3096f.css" data-n-g=""><link rel="preload" href="https://wokwi.com/_next/static/css/491037ee034f3b7e.css" as="style"><noscript data-n-css=""></noscript><style data-n-href="/_next/static/css/84ab9b81c1c9a0c0.css">.tabs_tabs__ztOIk{display:flex;align-items:center;flex-wrap:wrap;background-color:#ddd}@media screen and (min-width:1080px){.tabs_tabs__ztOIk{padding:10px 0 0 10px}}.tabs_tab__iRWK_{border:none;background:#ddd;border-radius:10px 10px 0 0;padding:8px 16px;max-height:2.1rem}.tabs_tab__iRWK_.tabs_active___gU2D{background:#fff;border:none;font-weight:700}.tabs_tab__iRWK_.tabs_modified__tU9Lp:after{content:"";display:inline-block;background:#000;border-radius:8px;margin-left:8px;width:8px;height:8px}.tabs_tab__iRWK_.tabs_errors__OLBf0{background:#a88}.tabs_dropdown__xOoyW{border:none;background:#ddd;padding:0;line-height:100%}.tabs_dropdown__xOoyW:hover{background:#fff}.tabs_dropdown__xOoyW.tabs_active___gU2D{background:#353;color:#fff}.tabs_dropdown__xOoyW.tabs_active___gU2D:hover{background:#8a8}.code-editor_wrapper__AEiSo{flex:1 1}.user-menu_altContent__PHtj5{display:inline-block;position:relative}.user-menu_alt1__swt4s,.user-menu_alt2__U4wD7{-webkit-animation:user-menu_show-hide__nPbXj 2s infinite;animation:user-menu_show-hide__nPbXj 2s infinite}.user-menu_alt1__swt4s{position:absolute;-webkit-animation-delay:1s;animation-delay:1s}@-webkit-keyframes user-menu_show-hide__nPbXj{0%{opacity:1}50%{opacity:1}50.01%{opacity:0}to{opacity:0}}@keyframes user-menu_show-hide__nPbXj{0%{opacity:1}50%{opacity:1}50.01%{opacity:0}to{opacity:0}}.share-modal_modalContent__biXYr{background:#333;display:flex;flex-direction:column;width:500px;max-width:100%}.share-modal_closeButton__O8vCJ{color:inherit;fill:currentColor}.share-modal_shareLinkContainer__TA_bA{display:flex}.share-modal_shareLinkContainer__TA_bA>input{flex:1 1;margin-right:8px}.pio-debugger_debugger__FmzYe{display:flex;flex:1 1;flex-direction:column;font-family:Courier New,Courier,monospace;height:0}.pio-debugger_current__DOX_g{background:blue}.pio-debugger_listing__qMfqG{flex:1 1;overflow:auto}.pio-debugger_listing__qMfqG pre{margin:0;display:flex}.pio-debugger_lineNumber__bwbeZ{margin-right:1em;color:gray}.pio-debugger_breakpoint__2hlYE{position:relative;-webkit-appearance:none;-moz-appearance:none;appearance:none;width:12px;border:none;background:transparent;cursor:pointer}.pio-debugger_breakpoint__2hlYE:checked:before,.pio-debugger_breakpoint__2hlYE:hover:before{content:" ";display:block;position:absolute;background-color:#460303;top:0;left:0;width:10px;height:10px;border-radius:50%}.pio-debugger_breakpoint__2hlYE:checked:before{background-color:red}.pio-debugger_fifo__LpGn8,.pio-debugger_registers__4PqDz span{white-space:pre-wrap}.diagram-part-pins_pinOverlay__It9jH{position:absolute;width:8px;height:8px;border:1px solid transparent}.diagram-part-pins_pinOverlay__It9jH:before{content:" ";display:block;position:absolute;top:0;left:0;right:0;bottom:0;z-index:20}.diagram-part-pins_pinOverlay__It9jH span{display:none;z-index:10;position:absolute;top:6px;background:#fff;color:#353;border:1px solid #353;transform:translate(calc(-50% + 4px),calc(-100% - 8px));padding:0 4px}.diagram-part-pins_pinOverlay__It9jH.diagram-part-pins_wiringActive__jVVKn{background:#353;border:1px solid #000;opacity:.4;z-index:1}.diagram-part-pins_pinOverlay__It9jH.diagram-part-pins_wiringHighlightPin__uAlSB{background:hsla(0,0%,100%,.8);border:1px solid #000;opacity:1}.diagram-part-pins_pinOverlay__It9jH:not(.diagram-part-pins_hide__APiBU):hover{background:#353;animation:diagram-part-pins_pin-overlay__PJ6vS 1s infinite alternate-reverse;border:1px solid #000;opacity:1}.diagram-part-pins_pinOverlay__It9jH:not(.diagram-part-pins_hide__APiBU):hover span{display:inline-block}@-webkit-keyframes diagram-part-pins_pin-overlay__PJ6vS{to{background:#7ac97a}}@keyframes diagram-part-pins_pin-overlay__PJ6vS{to{background:#7ac97a}}.custom-board-view_pixelated__fnld8{image-rendering:crisp-edges;-ms-interpolation-mode:nearest-neighbor;image-rendering:-moz-crisp-edges;image-rendering:pixelated}.diagram-part_diagramItem__ZeYe_{position:absolute}.diagram-part_diagramItem__ZeYe_.diagram-part_selectable__N65pi:hover{outline:2px dashed #353}.diagram-part_diagramItem__ZeYe_.diagram-part_editMode__gIx0Q:after{content:" ";position:absolute;top:0;right:0;bottom:0;left:0}.diagram-part_diagramItem__ZeYe_.diagram-part_active__exoHi:hover{outline:none}.diagram-part_diagramItem__ZeYe_.diagram-part_active__exoHi:before{content:" ";position:absolute;top:-2px;bottom:-2px;left:-2px;right:-2px;background:linear-gradient(90deg,#353 50%,transparent 0),linear-gradient(90deg,#353 50%,transparent 0),linear-gradient(0deg,#353 50%,transparent 0),linear-gradient(0deg,#353 50%,transparent 0);background-repeat:repeat-x,repeat-x,repeat-y,repeat-y;background-size:7px 2px,7px 2px,2px 7px,2px 7px;background-position:0 0,100% 100%,0 100%,100% 0;-webkit-animation:diagram-part_border-dance__0k6lc 4s linear infinite;animation:diagram-part_border-dance__0k6lc 4s linear infinite}@-webkit-keyframes diagram-part_border-dance__0k6lc{0%{background-position:0 0,100% 100%,0 100%,100% 0}to{background-position:100% 0,0 100%,0 0,100% 100%}}@keyframes diagram-part_border-dance__0k6lc{0%{background-position:0 0,100% 100%,0 100%,100% 0}to{background-position:100% 0,0 100%,0 0,100% 100%}}button.diagram-part_helpButton__c9JG6{position:absolute;color:#353}button.diagram-part_helpButton__c9JG6:hover{color:#5a5}.diagram-viewer_viewer__AHflp{position:relative;flex:1 1;display:flex;flex-direction:column;overflow:hidden;touch-action:none}.diagram-viewer_grid__Lkjzj,.diagram-viewer_rulerTop__Kr2bW{position:absolute;top:0;left:0;pointer-events:none}.diagram-viewer_rulerTop__Kr2bW{width:100%;height:50px}.diagram-viewer_rulerLeft__khuBO{position:absolute;width:50px;height:100%;top:0;left:0;pointer-events:none}.diagram-viewer_tickLabel__9bwL_{fill:#fff;pointer-events:none}.diagram-viewer_buttonGridUnits__Yjw7M,.diagram-viewer_tickLabel__9bwL_{font-family:Arial,Helvetica,sans-serif;font-size:8pt;font-weight:700;text-shadow:#000 1px 1px 2px,#444 0 0 5px}.diagram-viewer_buttonGridUnits__Yjw7M{position:absolute;right:5px;top:2px;background:none;border:none;padding:0;color:#fff}.diagram-viewer_buttonGridUnits__Yjw7M:hover{background:#444}.diagram-viewer_markerTop__xDvN6{height:50px;width:100%}.diagram-viewer_markerLeft__n0uTh,.diagram-viewer_markerTop__xDvN6{position:absolute;top:0;left:0;background-color:hsla(0,0%,60%,.5);pointer-events:none}.diagram-viewer_markerLeft__n0uTh{height:100%;width:50px}.diagram-viewer_connections__0hy0c{position:absolute;pointer-events:none}.diagram-viewer_connections__0hy0c.diagram-viewer_editMode__hgQxD g{pointer-events:visibleStroke}.diagram-viewer_connections__0hy0c path.diagram-viewer_outline__ZP2J5{stroke:none;stroke-dasharray:4px 4px;stroke-width:3px;-webkit-animation:diagram-viewer_outline-ants__k6mDq 1s linear infinite;animation:diagram-viewer_outline-ants__k6mDq 1s linear infinite}.diagram-viewer_connections__0hy0c g:hover path.diagram-viewer_outline__ZP2J5{stroke:#353}@-webkit-keyframes diagram-viewer_outline-ants__k6mDq{0%{stroke-dashoffset:0}to{stroke-dashoffset:24px}}@keyframes diagram-viewer_outline-ants__k6mDq{0%{stroke-dashoffset:0}to{stroke-dashoffset:24px}}.diagram-viewer_selectedPartInfo__U59S7{z-index:1;position:absolute;top:64px;left:4px;right:4px;padding:4px 8px;background:#fff;box-shadow:2px 2px 2px gray}.serial-plotter_tooltip__DIqtJ{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;background:#444;padding:1em;margin-left:20px;font-family:consolas;color:#fff;font-size:10px;pointer-events:none}.serial-plotter_tooltip__DIqtJ li,.serial-plotter_tooltip__DIqtJ ul{margin:0;padding:0;list-style-type:none}div.workbench-desktop_splitPane__B0r3f{height:auto;top:0;bottom:0;right:0;left:0}div.workbench-desktop_splitPane__B0r3f>.workbench-desktop_splitPane__B0r3f{height:100%}.workbench-desktop_container__c61v2{display:flex;position:relative;flex:1 1}.workbench-desktop_editor__L4Jxo{display:flex;flex-direction:column;flex:1 1;margin-bottom:2px}.workbench-desktop_splitPane__B0r3f .workbench-desktop_editor__L4Jxo{height:100%}.workbench-desktop_preview__Eeuqi{display:flex;flex-direction:column;height:100%;flex:1 1}div.workbench-desktop_diagramOnly__d81uo{flex:1 1;height:auto;top:0;bottom:0;right:0;left:0}.workbench-mobile_container__QXVNe{display:flex;flex-direction:column;position:relative;flex:1 1}.workbench-mobile_tab__lFXw9{flex:1 1;display:flex;flex-direction:column}.workbench-mobile_tab__lFXw9[hidden]{display:none}.workbench-mobile_editor__IOH7W{margin-bottom:2px}.workbench-mobile_diagram__4pv_n,.workbench-mobile_editor__IOH7W{display:flex;flex-direction:column;flex:1 1;height:0;min-height:100%}</style><script type="text/javascript" async="" src="./main_files/analytics.js.download"></script><script defer="" nomodule="" src="./main_files/polyfills-5cd94c89d3acac5f.js.download"></script><script src="./main_files/webpack-2de3922bfacf049b.js.download" defer=""></script><script src="./main_files/framework-79bce4a3a540b080.js.download" defer=""></script><script src="./main_files/main-890fedb11e2550a6.js.download" defer=""></script><script src="./main_files/_app-073c1dc12097ce32.js.download" defer=""></script><script src="./main_files/b2e984c5-febbc4ec3940268c.js.download" defer=""></script><script src="./main_files/2180-b27a4640ae1c64b9.js.download" defer=""></script><script src="./main_files/3955-3da1c8efa69276c6.js.download" defer=""></script><script src="./main_files/7730-59dcb474dce51a2e.js.download" defer=""></script><script src="./main_files/7984-71cbb95c63f9e239.js.download" defer=""></script><script src="./main_files/5268-388411a539956af1.js.download" defer=""></script><script src="./main_files/5458-a9c722b6b8524fbe.js.download" defer=""></script><script src="./main_files/1749-63e670f413d92b56.js.download" defer=""></script><script src="./main_files/2956-13e3a3273fb7f9a4.js.download" defer=""></script><script src="./main_files/5279-211a8add39f16ac3.js.download" defer=""></script><script src="./main_files/5675-ae978a771ccc26dc.js.download" defer=""></script><script src="./main_files/8479-392d80b7a7b46503.js.download" defer=""></script><script src="./main_files/8478-d8d4092ef64880ee.js.download" defer=""></script><script src="./main_files/2372-56d96884d0fdce91.js.download" defer=""></script><script src="./main_files/1967-eafd41143cffb22a.js.download" defer=""></script><script src="./main_files/8457-93b2bc4018649f89.js.download" defer=""></script><script src="./main_files/index-65d640b5428a5274.js.download" defer=""></script><script src="./main_files/_buildManifest.js.download" defer=""></script><script src="./main_files/_ssgManifest.js.download" defer=""></script><script src="./main_files/_middlewareManifest.js.download" defer=""></script><style id="jss-server-side">.jss1 {
  padding: 8px;
  font-size: 80%;
  background: #9c27b0;
  text-align: center;
}</style><style data-href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&amp;display=swap">@font-face{font-family:'Roboto';font-style:normal;font-weight:300;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmSU5fBBc-.woff) format('woff')}@font-face{font-family:'Roboto';font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOmCnqEu92Fr1Mu4mxM.woff) format('woff')}@font-face{font-family:'Roboto';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmEU9fBBc-.woff) format('woff')}@font-face{font-family:'Roboto';font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmWUlfBBc-.woff) format('woff')}@font-face{font-family:'Roboto';font-style:normal;font-weight:300;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmSU5fCRc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0460-052F,U+1C80-1C88,U+20B4,U+2DE0-2DFF,U+A640-A69F,U+FE2E-FE2F}@font-face{font-family:'Roboto';font-style:normal;font-weight:300;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmSU5fABc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}@font-face{font-family:'Roboto';font-style:normal;font-weight:300;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmSU5fCBc4AMP6lbBP.woff2) format('woff2');unicode-range:U+1F00-1FFF}@font-face{font-family:'Roboto';font-style:normal;font-weight:300;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmSU5fBxc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0370-03FF}@font-face{font-family:'Roboto';font-style:normal;font-weight:300;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmSU5fCxc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+1EA0-1EF9,U+20AB}@font-face{font-family:'Roboto';font-style:normal;font-weight:300;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmSU5fChc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF}@font-face{font-family:'Roboto';font-style:normal;font-weight:300;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmSU5fBBc4AMP6lQ.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}@font-face{font-family:'Roboto';font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOmCnqEu92Fr1Mu72xKKTU1Kvnz.woff2) format('woff2');unicode-range:U+0460-052F,U+1C80-1C88,U+20B4,U+2DE0-2DFF,U+A640-A69F,U+FE2E-FE2F}@font-face{font-family:'Roboto';font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOmCnqEu92Fr1Mu5mxKKTU1Kvnz.woff2) format('woff2');unicode-range:U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}@font-face{font-family:'Roboto';font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOmCnqEu92Fr1Mu7mxKKTU1Kvnz.woff2) format('woff2');unicode-range:U+1F00-1FFF}@font-face{font-family:'Roboto';font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOmCnqEu92Fr1Mu4WxKKTU1Kvnz.woff2) format('woff2');unicode-range:U+0370-03FF}@font-face{font-family:'Roboto';font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOmCnqEu92Fr1Mu7WxKKTU1Kvnz.woff2) format('woff2');unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+1EA0-1EF9,U+20AB}@font-face{font-family:'Roboto';font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOmCnqEu92Fr1Mu7GxKKTU1Kvnz.woff2) format('woff2');unicode-range:U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF}@font-face{font-family:'Roboto';font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOmCnqEu92Fr1Mu4mxKKTU1Kg.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}@font-face{font-family:'Roboto';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmEU9fCRc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0460-052F,U+1C80-1C88,U+20B4,U+2DE0-2DFF,U+A640-A69F,U+FE2E-FE2F}@font-face{font-family:'Roboto';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmEU9fABc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}@font-face{font-family:'Roboto';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmEU9fCBc4AMP6lbBP.woff2) format('woff2');unicode-range:U+1F00-1FFF}@font-face{font-family:'Roboto';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmEU9fBxc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0370-03FF}@font-face{font-family:'Roboto';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmEU9fCxc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+1EA0-1EF9,U+20AB}@font-face{font-family:'Roboto';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmEU9fChc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF}@font-face{font-family:'Roboto';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmEU9fBBc4AMP6lQ.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}@font-face{font-family:'Roboto';font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmWUlfCRc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0460-052F,U+1C80-1C88,U+20B4,U+2DE0-2DFF,U+A640-A69F,U+FE2E-FE2F}@font-face{font-family:'Roboto';font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmWUlfABc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}@font-face{font-family:'Roboto';font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmWUlfCBc4AMP6lbBP.woff2) format('woff2');unicode-range:U+1F00-1FFF}@font-face{font-family:'Roboto';font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmWUlfBxc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0370-03FF}@font-face{font-family:'Roboto';font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmWUlfCxc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+1EA0-1EF9,U+20AB}@font-face{font-family:'Roboto';font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmWUlfChc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF}@font-face{font-family:'Roboto';font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v29/KFOlCnqEu92Fr1MmWUlfBBc4AMP6lQ.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}</style><style data-jss="" data-meta="makeStyles">
.jss1 {
  padding: 8px;
  font-size: 80%;
  background: #9c27b0;
  text-align: center;
}
</style><style data-jss="" data-meta="makeStyles">
.jss4 {
  padding: 4px 0;
  min-width: 28px;
}
</style><style data-jss="" data-meta="makeStyles">
.jss5 {
  min-height: 96px;
}
</style><style data-jss="" data-meta="makeStyles">
.jss6 {
  min-height: 96px;
}
</style><style data-jss="" data-meta="makeStyles">
.jss7 {
  flex: 1;
  color: black;
  display: flex;
  position: relative;
  background: #ddd;
  flex-direction: column;
}
.jss8 {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 10;
  position: fixed;
}
</style><style data-jss="" data-meta="makeStyles">
.jss2 {
  margin: 8px;
}
.jss3 {
  display: inline-flex;
  min-width: initial;
  margin-right: 8px;
}
</style><style type="text/css" data-styled-jsx=""></style><link as="script" rel="prefetch" href="./main_files/[template]-b56b25b357bdbe2c.js.download"><style data-styled="active" data-styled-version="5.2.0"></style><script async="async" type="text/javascript" src="./main_files/editor.main.js.download"></script><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./main_files/editor.main.css"><script async="async" type="text/javascript" src="./main_files/editor.main.nls.js.download"></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-info:before { content: '\ea74'; }
.codicon-close:before { content: '\ea76'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }

			.monaco-scrollable-element > .shadow.top {
				box-shadow: #dddddd 0 6px 6px -6px inset;
			}

			.monaco-scrollable-element > .shadow.left {
				box-shadow: #dddddd 6px 0 6px -6px inset;
			}

			.monaco-scrollable-element > .shadow.top.left {
				box-shadow: #dddddd 6px 6px 6px -6px inset;
			}
		

			.monaco-scrollable-element > .scrollbar > .slider {
				background: rgba(100, 100, 100, 0.4);
			}
		

			.monaco-scrollable-element > .scrollbar > .slider:hover {
				background: rgba(100, 100, 100, 0.7);
			}
		

			.monaco-scrollable-element > .scrollbar > .slider.active {
				background: rgba(0, 0, 0, 0.6);
			}
		
.monaco-editor .minimap-slider .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.2); }
.monaco-editor .minimap-slider:hover .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.35); }
.monaco-editor .minimap-slider.active .minimap-slider-horizontal { background: rgba(0, 0, 0, 0.3); }
.monaco-editor .minimap-shadow-visible { box-shadow: #dddddd -6px 0 6px -6px inset; }
.monaco-editor .scroll-decoration { box-shadow: #dddddd 0 6px 6px -6px inset; }
.monaco-editor .focused .selected-text { background-color: #add6ff; }
.monaco-editor .selected-text { background-color: #e5ebf1; }
.monaco-editor, .monaco-editor-background, .monaco-editor .inputarea.ime-input { background-color: #fffffe; }
.monaco-editor, .monaco-editor .inputarea.ime-input { color: #000000; }
.monaco-editor .margin { background-color: #fffffe; }
.monaco-editor .rangeHighlight { background-color: rgba(253, 255, 0, 0.2); }
.monaco-editor .symbolHighlight { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .mtkw { color: rgba(51, 51, 51, 0.2) !important; }
.monaco-editor .mtkz { color: rgba(51, 51, 51, 0.2) !important; }
.monaco-editor .view-overlays .current-line { border: 2px solid #eeeeee; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #eeeeee; }
.monaco-editor .line-numbers { color: #237893; }
.monaco-editor .line-numbers.active-line-number { color: #0b216f; }
.monaco-editor .view-ruler { box-shadow: 1px 0 0 0 #d3d3d3 inset; }
.monaco-editor .cursors-layer .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #0431fa; }
.monaco-editor .bracket-highlighting-1 { color: #319331; }
.monaco-editor .bracket-highlighting-2 { color: #7b3814; }
.monaco-editor .bracket-highlighting-3 { color: #0431fa; }
.monaco-editor .bracket-highlighting-4 { color: #319331; }
.monaco-editor .bracket-highlighting-5 { color: #7b3814; }
.monaco-editor .bracket-highlighting-6 { color: #0431fa; }
.monaco-editor .bracket-highlighting-7 { color: #319331; }
.monaco-editor .bracket-highlighting-8 { color: #7b3814; }
.monaco-editor .bracket-highlighting-9 { color: #0431fa; }
.monaco-editor .bracket-highlighting-10 { color: #319331; }
.monaco-editor .bracket-highlighting-11 { color: #7b3814; }
.monaco-editor .bracket-highlighting-12 { color: #0431fa; }
.monaco-editor .bracket-highlighting-13 { color: #319331; }
.monaco-editor .bracket-highlighting-14 { color: #7b3814; }
.monaco-editor .bracket-highlighting-15 { color: #0431fa; }
.monaco-editor .bracket-highlighting-16 { color: #319331; }
.monaco-editor .bracket-highlighting-17 { color: #7b3814; }
.monaco-editor .bracket-highlighting-18 { color: #0431fa; }
.monaco-editor .bracket-highlighting-19 { color: #319331; }
.monaco-editor .bracket-highlighting-20 { color: #7b3814; }
.monaco-editor .bracket-highlighting-21 { color: #0431fa; }
.monaco-editor .bracket-highlighting-22 { color: #319331; }
.monaco-editor .bracket-highlighting-23 { color: #7b3814; }
.monaco-editor .bracket-highlighting-24 { color: #0431fa; }
.monaco-editor .bracket-highlighting-25 { color: #319331; }
.monaco-editor .bracket-highlighting-26 { color: #7b3814; }
.monaco-editor .bracket-highlighting-27 { color: #0431fa; }
.monaco-editor .bracket-highlighting-28 { color: #319331; }
.monaco-editor .bracket-highlighting-29 { color: #7b3814; }
.monaco-editor .ghost-text-decoration { color: rgba(0, 0, 0, 0.47) !important; }
.monaco-editor .ghost-text-decoration-preview { color: rgba(0, 0, 0, 0.47) !important; }
.monaco-editor .suggest-preview-text .ghost-text { color: rgba(0, 0, 0, 0.47) !important; }
.monaco-editor .lines-content .core-guide-indent { box-shadow: 1px 0 0 0 #d3d3d3 inset; }
.monaco-editor .lines-content .core-guide-indent-active { box-shadow: 1px 0 0 0 #939393 inset; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor.vs .valueSetReplacement { outline: solid 2px #b9b9b9; }
.codicon.codicon-symbol-array { color: #616161; }
.codicon.codicon-symbol-boolean { color: #616161; }
.codicon.codicon-symbol-class { color: #d67e00; }
.codicon.codicon-symbol-method { color: #652d90; }
.codicon.codicon-symbol-color { color: #616161; }
.codicon.codicon-symbol-constant { color: #616161; }
.codicon.codicon-symbol-constructor { color: #652d90; }

			.codicon.codicon-symbol-value,.codicon.codicon-symbol-enum { color: #d67e00; }
.codicon.codicon-symbol-enum-member { color: #007acc; }
.codicon.codicon-symbol-event { color: #d67e00; }
.codicon.codicon-symbol-field { color: #007acc; }
.codicon.codicon-symbol-file { color: #616161; }
.codicon.codicon-symbol-folder { color: #616161; }
.codicon.codicon-symbol-function { color: #652d90; }
.codicon.codicon-symbol-interface { color: #007acc; }
.codicon.codicon-symbol-key { color: #616161; }
.codicon.codicon-symbol-keyword { color: #616161; }
.codicon.codicon-symbol-module { color: #616161; }
.codicon.codicon-symbol-namespace { color: #616161; }
.codicon.codicon-symbol-null { color: #616161; }
.codicon.codicon-symbol-number { color: #616161; }
.codicon.codicon-symbol-object { color: #616161; }
.codicon.codicon-symbol-operator { color: #616161; }
.codicon.codicon-symbol-package { color: #616161; }
.codicon.codicon-symbol-property { color: #616161; }
.codicon.codicon-symbol-reference { color: #616161; }
.codicon.codicon-symbol-snippet { color: #616161; }
.codicon.codicon-symbol-string { color: #616161; }
.codicon.codicon-symbol-struct { color: #616161; }
.codicon.codicon-symbol-text { color: #616161; }
.codicon.codicon-symbol-type-parameter { color: #616161; }
.codicon.codicon-symbol-unit { color: #616161; }
.codicon.codicon-symbol-variable { color: #007acc; }
.monaco-editor .accessibilityHelpWidget { background-color: #f3f3f3; }
.monaco-editor .accessibilityHelpWidget { color: #616161; }
.monaco-editor .accessibilityHelpWidget { box-shadow: 0 2px 8px rgba(0, 0, 0, 0.16); }
.monaco-editor .tokens-inspect-widget { border: 1px solid #c8c8c8; }
.monaco-editor .tokens-inspect-widget .tokens-inspect-separator { background-color: #c8c8c8; }
.monaco-editor .tokens-inspect-widget { background-color: #f3f3f3; }
.monaco-editor .tokens-inspect-widget { color: #616161; }
.monaco-link { color: #006ab1; }
.monaco-link:hover { color: #006ab1; }

			.monaco-editor .zone-widget .codicon.codicon-error,
			.markers-panel .marker-icon.codicon.codicon-error,
			.text-search-provider-messages .providerMessage .codicon.codicon-error,
			.extensions-viewlet > .extensions .codicon.codicon-error {
				color: #e51400;
			}
		

			.monaco-editor .zone-widget .codicon.codicon-warning,
			.markers-panel .marker-icon.codicon.codicon-warning,
			.extensions-viewlet > .extensions .codicon.codicon-warning,
			.extension-editor .codicon.codicon-warning,
			.text-search-provider-messages .providerMessage .codicon.codicon-warning,
			.preferences-editor .codicon.codicon-warning {
				color: #bf8803;
			}
		

			.monaco-editor .zone-widget .codicon.codicon-info,
			.markers-panel .marker-icon.codicon.codicon-info,
			.extensions-viewlet > .extensions .codicon.codicon-info,
			.text-search-provider-messages .providerMessage .codicon.codicon-info,
			.extension-editor .codicon.codicon-info {
				color: #1a85ff;
			}
		
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23bf8803'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%231a85ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor.showDeprecated .squiggly-inline-deprecated { text-decoration: line-through; text-decoration-color: #000000}
.monaco-editor .bracket-match { background-color: rgba(0, 100, 0, 0.1); }
.monaco-editor .bracket-match { border: 1px solid #b9b9b9; }

		.monaco-editor .contentWidgets .codicon.codicon-light-bulb {
			color: #ddb100;
			background-color: rgba(255, 255, 254, 0.7);
		}

		.monaco-editor .contentWidgets .codicon.codicon-lightbulb-autofix {
			color: #007acc;
			background-color: rgba(255, 255, 254, 0.7);
		}
.monaco-editor .findOptionsWidget { background-color: #f3f3f3; }
.monaco-editor .findOptionsWidget { color: #616161; }
.monaco-editor .findOptionsWidget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.16); }
.monaco-editor .linked-editing-decoration { background: rgba(255, 0, 0, 0.3); border-left-color: rgba(255, 0, 0, 0.3); }
.monaco-editor .detected-link-active { color: #0000ff !important; }
.monaco-editor .focused .selectionHighlight { background-color: rgba(173, 214, 255, 0.3); }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }
.monaco-editor .wordHighlight { background-color: rgba(87, 87, 87, 0.25); }
.monaco-editor .wordHighlightStrong { background-color: rgba(14, 99, 156, 0.25); }
.monaco-editor .goto-definition-link { color: #0000ff !important; }
.monaco-diff-editor .diff-review-line-number { color: #237893; }
.monaco-diff-editor .diff-review-shadow { box-shadow: #dddddd 0 -6px 6px -6px inset; }
.monaco-editor .parameter-hints-widget { border: 1px solid #c8c8c8; }
.monaco-editor .parameter-hints-widget.multiple .body { border-left: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .parameter-hints-widget .signature.has-docs { border-bottom: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .parameter-hints-widget { background-color: #f3f3f3; }
.monaco-editor .parameter-hints-widget a { color: #006ab1; }
.monaco-editor .parameter-hints-widget a:hover { color: #006ab1; }
.monaco-editor .parameter-hints-widget { color: #616161; }
.monaco-editor .parameter-hints-widget code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor .parameter-hints-widget .parameter.active { color: #0066bf}
.monaco-editor .line-insert, .monaco-editor .char-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-diff-editor .line-insert, .monaco-diff-editor .char-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .inline-added-margin-view-zone { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .line-delete, .monaco-editor .char-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-diff-editor .line-delete, .monaco-diff-editor .char-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-editor .inline-deleted-margin-view-zone { background-color: rgba(255, 0, 0, 0.2); }
.monaco-diff-editor.side-by-side .editor.modified { box-shadow: -6px 0 5px -5px #dddddd; }

			.monaco-diff-editor .diffViewport {
				background: rgba(100, 100, 100, 0.4);
			}
		

			.monaco-diff-editor .diffViewport:hover {
				background: rgba(100, 100, 100, 0.7);
			}
		

			.monaco-diff-editor .diffViewport:active {
				background: rgba(0, 0, 0, 0.6);
			}
		

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(34, 34, 34, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(34, 34, 34, 0.2) 50%, rgba(34, 34, 34, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.16); }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(184, 184, 184, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #0090f1; }
.monaco-editor .folded-background { background-color: rgba(173, 214, 255, 0.3); }

		.monaco-editor .cldr.codicon.codicon-folding-expanded,
		.monaco-editor .cldr.codicon.codicon-folding-collapsed {
			color: #424242 !important;
		}
		
.monaco-hover .hover-contents a.code-link span { color: #006ab1; }
.monaco-hover .hover-contents a.code-link span:hover { color: #006ab1; }
.monaco-editor .hoverHighlight { background-color: rgba(173, 214, 255, 0.15); }
.monaco-editor .monaco-hover { background-color: #f3f3f3; }
.monaco-editor .monaco-hover { border: 1px solid #c8c8c8; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover a { color: #006ab1; }
.monaco-editor .monaco-hover a:hover { color: #006ab1; }
.monaco-editor .monaco-hover { color: #616161; }
.monaco-editor .monaco-hover .hover-row .actions { background-color: #e7e7e7; }
.monaco-editor .monaco-hover code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor { --vscode-foreground: #616161;
--vscode-errorForeground: #a1260d;
--vscode-descriptionForeground: #717171;
--vscode-icon-foreground: #424242;
--vscode-focusBorder: #0090f1;
--vscode-textSeparator-foreground: rgba(0, 0, 0, 0.18);
--vscode-textLink-foreground: #006ab1;
--vscode-textLink-activeForeground: #006ab1;
--vscode-textPreformat-foreground: #a31515;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(220, 220, 220, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.16);
--vscode-input-background: #ffffff;
--vscode-input-foreground: #616161;
--vscode-inputOption-activeBorder: rgba(0, 122, 204, 0);
--vscode-inputOption-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-inputOption-activeBackground: rgba(0, 144, 241, 0.2);
--vscode-inputOption-activeForeground: #000000;
--vscode-input-placeholderForeground: rgba(97, 97, 97, 0.5);
--vscode-inputValidation-infoBackground: #d6ecf2;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #f6f5d2;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #f2dede;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #ffffff;
--vscode-dropdown-border: #cecece;
--vscode-checkbox-background: #ffffff;
--vscode-checkbox-border: #cecece;
--vscode-button-foreground: #ffffff;
--vscode-button-background: #007acc;
--vscode-button-hoverBackground: #0062a3;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #5f6a79;
--vscode-button-secondaryHoverBackground: #4c5561;
--vscode-badge-background: #c4c4c4;
--vscode-badge-foreground: #333333;
--vscode-scrollbar-shadow: #dddddd;
--vscode-scrollbarSlider-background: rgba(100, 100, 100, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(0, 0, 0, 0.6);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #e51400;
--vscode-editorWarning-foreground: #bf8803;
--vscode-editorInfo-foreground: #1a85ff;
--vscode-editorHint-foreground: #6c6c6c;
--vscode-sash-hoverBorder: #0090f1;
--vscode-editor-background: #fffffe;
--vscode-editor-foreground: #000000;
--vscode-editorWidget-background: #f3f3f3;
--vscode-editorWidget-foreground: #616161;
--vscode-editorWidget-border: #c8c8c8;
--vscode-quickInput-background: #f3f3f3;
--vscode-quickInput-foreground: #616161;
--vscode-quickInputTitle-background: rgba(0, 0, 0, 0.06);
--vscode-pickerGroup-foreground: #0066bf;
--vscode-pickerGroup-border: #cccedb;
--vscode-keybindingLabel-background: rgba(221, 221, 221, 0.4);
--vscode-keybindingLabel-foreground: #555555;
--vscode-keybindingLabel-border: rgba(204, 204, 204, 0.4);
--vscode-keybindingLabel-bottomBorder: rgba(187, 187, 187, 0.4);
--vscode-editor-selectionBackground: #add6ff;
--vscode-editor-inactiveSelectionBackground: #e5ebf1;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.3);
--vscode-editor-findMatchBackground: #a8ac94;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(180, 180, 180, 0.3);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-editor-hoverHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editorHoverWidget-background: #f3f3f3;
--vscode-editorHoverWidget-foreground: #616161;
--vscode-editorHoverWidget-border: #c8c8c8;
--vscode-editorHoverWidget-statusBarBackground: #e7e7e7;
--vscode-editorLink-activeForeground: #0000ff;
--vscode-editorInlayHint-foreground: rgba(51, 51, 51, 0.8);
--vscode-editorInlayHint-background: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-typeForeground: rgba(51, 51, 51, 0.8);
--vscode-editorInlayHint-typeBackground: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-parameterForeground: rgba(51, 51, 51, 0.8);
--vscode-editorInlayHint-parameterBackground: rgba(196, 196, 196, 0.3);
--vscode-editorLightBulb-foreground: #ddb100;
--vscode-editorLightBulbAutoFix-foreground: #007acc;
--vscode-diffEditor-insertedTextBackground: rgba(155, 185, 85, 0.2);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.2);
--vscode-diffEditor-diagonalFill: rgba(34, 34, 34, 0.2);
--vscode-list-focusOutline: #0090f1;
--vscode-list-activeSelectionBackground: #0060c0;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #e4e6f1;
--vscode-list-hoverBackground: #f0f0f0;
--vscode-list-dropBackground: #d6ebff;
--vscode-list-highlightForeground: #0066bf;
--vscode-list-focusHighlightForeground: #9dddff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #b01011;
--vscode-list-warningForeground: #855f00;
--vscode-listFilterWidget-background: #efc1ad;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #a9a9a9;
--vscode-tree-tableColumnsBorder: rgba(97, 97, 97, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(97, 97, 97, 0.04);
--vscode-list-deemphasizedForeground: #8e8e90;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #0060c0;
--vscode-menu-foreground: #616161;
--vscode-menu-background: #ffffff;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #0060c0;
--vscode-menu-separatorBackground: #888888;
--vscode-toolbar-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-toolbar-activeBackground: rgba(166, 166, 166, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(10, 50, 100, 0.2);
--vscode-editor-snippetFinalTabstopHighlightBorder: rgba(10, 50, 100, 0.5);
--vscode-breadcrumb-foreground: rgba(97, 97, 97, 0.8);
--vscode-breadcrumb-background: #fffffe;
--vscode-breadcrumb-focusForeground: #4e4e4e;
--vscode-breadcrumb-activeSelectionForeground: #4e4e4e;
--vscode-breadcrumbPicker-background: #f3f3f3;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-unicodeForeground: rgba(209, 134, 22, 0.49);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #c9c9c9;
--vscode-minimap-selectionHighlight: #add6ff;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #bf8803;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimap-unicodeHighlight: #d18616;
--vscode-minimapSlider-background: rgba(100, 100, 100, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(0, 0, 0, 0.3);
--vscode-problemsErrorIcon-foreground: #e51400;
--vscode-problemsWarningIcon-foreground: #bf8803;
--vscode-problemsInfoIcon-foreground: #1a85ff;
--vscode-charts-foreground: #616161;
--vscode-charts-lines: rgba(97, 97, 97, 0.5);
--vscode-charts-red: #e51400;
--vscode-charts-blue: #1a85ff;
--vscode-charts-yellow: #bf8803;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #388a34;
--vscode-charts-purple: #652d90;
--vscode-editor-lineHighlightBorder: #eeeeee;
--vscode-editor-rangeHighlightBackground: rgba(253, 255, 0, 0.2);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #000000;
--vscode-editorWhitespace-foreground: rgba(51, 51, 51, 0.2);
--vscode-editorIndentGuide-background: #d3d3d3;
--vscode-editorIndentGuide-activeBackground: #939393;
--vscode-editorLineNumber-foreground: #237893;
--vscode-editorActiveLineNumber-foreground: #0b216f;
--vscode-editorLineNumber-activeForeground: #0b216f;
--vscode-editorRuler-foreground: #d3d3d3;
--vscode-editorCodeLens-foreground: #919191;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #b9b9b9;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #fffffe;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.47);
--vscode-editorGhostText-foreground: rgba(0, 0, 0, 0.47);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #bf8803;
--vscode-editorOverviewRuler-infoForeground: #1a85ff;
--vscode-editorBracketHighlight-foreground1: #0431fa;
--vscode-editorBracketHighlight-foreground2: #319331;
--vscode-editorBracketHighlight-foreground3: #7b3814;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket.foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #cea33d;
--vscode-symbolIcon-arrayForeground: #616161;
--vscode-symbolIcon-booleanForeground: #616161;
--vscode-symbolIcon-classForeground: #d67e00;
--vscode-symbolIcon-colorForeground: #616161;
--vscode-symbolIcon-constantForeground: #616161;
--vscode-symbolIcon-constructorForeground: #652d90;
--vscode-symbolIcon-enumeratorForeground: #d67e00;
--vscode-symbolIcon-enumeratorMemberForeground: #007acc;
--vscode-symbolIcon-eventForeground: #d67e00;
--vscode-symbolIcon-fieldForeground: #007acc;
--vscode-symbolIcon-fileForeground: #616161;
--vscode-symbolIcon-folderForeground: #616161;
--vscode-symbolIcon-functionForeground: #652d90;
--vscode-symbolIcon-interfaceForeground: #007acc;
--vscode-symbolIcon-keyForeground: #616161;
--vscode-symbolIcon-keywordForeground: #616161;
--vscode-symbolIcon-methodForeground: #652d90;
--vscode-symbolIcon-moduleForeground: #616161;
--vscode-symbolIcon-namespaceForeground: #616161;
--vscode-symbolIcon-nullForeground: #616161;
--vscode-symbolIcon-numberForeground: #616161;
--vscode-symbolIcon-objectForeground: #616161;
--vscode-symbolIcon-operatorForeground: #616161;
--vscode-symbolIcon-packageForeground: #616161;
--vscode-symbolIcon-propertyForeground: #616161;
--vscode-symbolIcon-referenceForeground: #616161;
--vscode-symbolIcon-snippetForeground: #616161;
--vscode-symbolIcon-stringForeground: #616161;
--vscode-symbolIcon-structForeground: #616161;
--vscode-symbolIcon-textForeground: #616161;
--vscode-symbolIcon-typeParameterForeground: #616161;
--vscode-symbolIcon-unitForeground: #616161;
--vscode-symbolIcon-variableForeground: #007acc;
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.25);
--vscode-editor-wordHighlightStrongBackground: rgba(14, 99, 156, 0.25);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-peekViewTitle-background: rgba(26, 133, 255, 0.1);
--vscode-peekViewTitleLabel-foreground: #000000;
--vscode-peekViewTitleDescription-foreground: #616161;
--vscode-peekView-border: #1a85ff;
--vscode-peekViewResult-background: #f3f3f3;
--vscode-peekViewResult-lineForeground: #646465;
--vscode-peekViewResult-fileForeground: #1e1e1e;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #6c6c6c;
--vscode-peekViewEditor-background: #f2f8fc;
--vscode-peekViewEditorGutter-background: #f2f8fc;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(245, 216, 2, 0.87);
--vscode-editorMarkerNavigationError-background: #e51400;
--vscode-editorMarkerNavigationError-headerBackground: rgba(229, 20, 0, 0.1);
--vscode-editorMarkerNavigationWarning-background: #bf8803;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(191, 136, 3, 0.1);
--vscode-editorMarkerNavigationInfo-background: #1a85ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(26, 133, 255, 0.1);
--vscode-editorMarkerNavigation-background: #fffffe;
--vscode-editorHoverWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-background: #f3f3f3;
--vscode-editorSuggestWidget-border: #c8c8c8;
--vscode-editorSuggestWidget-foreground: #000000;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #0060c0;
--vscode-editorSuggestWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-focusHighlightForeground: #9dddff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(0, 0, 0, 0.5);
--vscode-editor-foldBackground: rgba(173, 214, 255, 0.3);
--vscode-editorGutter-foldingControlForeground: #424242; }

.mtk1 { color: #000000; }
.mtk2 { color: #fffffe; }
.mtk3 { color: #808080; }
.mtk4 { color: #97009c; }
.mtk5 { color: #e97366; }
.mtk6 { color: #00979c; }
.mtk7 { color: #5e6d03; }
.mtk8 { color: #ff0000; }
.mtk9 { color: #0451a5; }
.mtk10 { color: #0000ff; }
.mtk11 { color: #098658; }
.mtk12 { color: #008000; }
.mtk13 { color: #727c81; }
.mtk14 { color: #dd0000; }
.mtk15 { color: #383838; }
.mtk16 { color: #cd3131; }
.mtk17 { color: #863b00; }
.mtk18 { color: #af00db; }
.mtk19 { color: #800000; }
.mtk20 { color: #e00000; }
.mtk21 { color: #3030c0; }
.mtk22 { color: #666666; }
.mtk23 { color: #778899; }
.mtk24 { color: #c700c7; }
.mtk25 { color: #a31515; }
.mtk26 { color: #4f76ac; }
.mtk27 { color: #008080; }
.mtk28 { color: #001188; }
.mtk29 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }</style><style type="text/css" media="screen">
		.monaco-editor .codelens-decoration._ee1f62 { line-height: 19px; font-size: 12px; padding-right: 6px; font-feature-settings: var(--codelens-font-features_ee1f62) }
		.monaco-editor .codelens-decoration._ee1f62 span.codicon { line-height: 19px; font-size: 12px; }
		</style><style type="text/css" media="screen"></style></head><body style=""><div id="__next" data-reactroot=""><div class="jsx-4253649316 page-container"><header class="jsx-31981644"><div role="banner" class="jsx-31981644 toolbar"><a class="jsx-31981644 logo" href="https://wokwi.com/"><svg width="80" height="24" viewBox="0 0 69.532 16.413"><g fill="#fff"><path d="M4.192 15.53c-.63-.737-.765-1.863-.32-2.684.405-.748.346-1.136-.583-3.84-.937-2.73-1.116-3.05-1.935-3.455-1.916-.949-1.765-3.452.242-4 1.892-.518 3.374 1.385 2.418 3.105-.416.75-.36 1.113.593 3.865.969 2.796 1.125 3.072 1.964 3.457 1.192.548 1.62 1.883.969 3.024-.65 1.14-2.566 1.442-3.348.528zm1.912-1.003c.465-.38.426-.796-.103-1.098-.238-.136-.545-.186-.681-.111-.423.23-.407 1.014.025 1.26.226.129.567.106.76-.05zM2.612 4.17c.346-.189.224-1.077-.18-1.308-.337-.192-.995.269-.98.687.013.386.809.812 1.16.621zM11.945 15c-.63-.737-.765-1.863-.32-2.684.405-.748.346-1.136-.583-3.84-.937-2.73-1.116-3.05-1.935-3.455-1.916-.949-1.765-3.452.242-4 1.892-.518 3.374 1.385 2.418 3.105-.416.75-.36 1.113.593 3.865.969 2.796 1.125 3.072 1.964 3.457 1.192.548 1.62 1.883.969 3.024-.65 1.14-2.566 1.442-3.348.528zm1.912-1.003c.465-.38.426-.796-.103-1.098-.238-.136-.545-.186-.681-.111-.423.23-.407 1.014.025 1.26.226.129.567.106.76-.05zM10.365 3.64c.346-.189.224-1.077-.18-1.308-.337-.192-.995.269-.98.687.013.386.809.812 1.16.621z"></path><path d="M4.543 16.22c-2.027-1.187-1.3-4.185 1.015-4.185.75 0 .816-.177 1.864-1.169s2.833-2.627 4.035-3.221c.324.459.571 1.614.607 1.748-.773 0-2.75 1.515-3.588 2.537-.81.989-.985 1.4-.928 2.188.052.73-.081 1.111-.542 1.54-.779.729-1.786.958-2.463.562zm1.56-1.695c.215-.56-.025-.902-.634-.902-.594 0-.896.408-.693.938.198.516 1.125.49 1.327-.036zM13.185 12.06s.283-.565 1.392-3.717c1.44-4.077 1.509-4.406 1.096-5.263-.887-1.84.835-3.684 2.691-2.88.694.3.931.585 1.236 1.49.332.983.303 1.19-.244 1.72-.342.331-.896.716-1.232.856-.47.196-.971 1.255-2.185 4.618-1.443 3.997-1.06 2.817-.67 3.541.961 1.79-.26.492-2.084-.365zm5.066-9.85c-.006-.6-.355-.829-.922-.605-.254.101-.485.309-.512.462-.085.474.537.951 1 .768.241-.095.437-.377.434-.624z"></path><g><path d="M26.397 15.57q-2.378.363-4.232-.922-1.97-1.37-2.308-3.953-.413-3.147.978-5.985 1.557-3.15 4.441-3.59 2.774-.424 4.3.717 1.592 1.186 1.988 4.205.413 3.147-.84 5.918-1.443 3.17-4.327 3.61zm-.876-12.586q-2.066.315-3.209 2.753-1.057 2.24-.735 4.695.23 1.756 1.58 2.672 1.292.861 2.995.601 2.05-.312 3.09-2.744.928-2.173.602-4.657-.285-2.173-1.303-2.918-.971-.715-3.02-.402zM35.637.98a.872.872 0 00-.652.275.947.947 0 00-.257.671c0 1.224-.039 3.081-.102 5.354.318-.509.773-.846 1.271-.896a2.28 2.28 0 01.467 0 63.88 63.88 0 01.082-1.684c.073-1.255.11-2.18.11-2.774a.93.93 0 00-.267-.67.853.853 0 00-.652-.276zm6.825.156c-.257 0-.49.12-.698.358l-2.636 3.06a52.882 52.882 0 01-1.944 2.099c.547.32.914.88 1.074 1.479.945-.925 1.887-1.847 2.771-2.816 1.58-1.752 2.37-2.83 2.37-3.234a.898.898 0 00-.284-.67.912.912 0 00-.653-.276zm-4.208 8.307c-.12.378-.352.707-.712.92a1.978 1.978 0 01-.754.26l2.33 2.345c1.721 1.635 3.047 2.453 3.978 2.453.264 0 .475-.117.634-.35.129-.19.193-.388.193-.597 0-.447-.242-.75-.726-.91a3.81 3.81 0 01-1.13-.605l-.964-.81a106.213 106.213 0 01-2.849-2.706zm-3.69.229a210.995 210.995 0 00-.093 5.105c0 .294.085.567.257.818.208.306.487.459.836.459.532 0 .8-.303.8-.91l.007-4.509c-.606-.039-1.208-.324-1.664-.783a3.926 3.926 0 01-.143-.18zm1.333-3.288c2.338-.235 3.256 3.024 1.645 3.98-.912.54-2.076.252-2.835-.512-.473-.56-.589-.946-.47-1.564.202-1.047.88-1.826 1.66-1.904zm-.262 2.289c.156.58.552.714 1.044.355.48-.35.484-.858.007-1.167-.464-.3-1.198.267-1.051.812zM57.077 15.93c-.282 0-.53-.08-.744-.239-.245-.184-.367-.41-.367-.68-.282-.74-.46-1.344-.533-1.81-.074-.465-.316-1.784-.726-3.958-.312-1.648-.52-2.97-.625-3.969-.545 2.021-1.13 3.733-1.754 5.135-.723 1.623-1.191 2.894-1.406 3.812.074.141.11.279.11.414 0 .275-.122.502-.367.68-.22.165-.471.248-.753.248-.827 0-1.24-.371-1.24-1.112l-.285-1.167-1.001-4.5c-.398-1.52-1.078-3.697-2.04-6.532a1.225 1.225 0 01-.064-.368c0-.569.322-.854.965-.854.398 0 .704.218.918.652.11.22.334.855.67 1.902.362 1.108.723 2.443 1.085 4.005l.89 4.06c.656-1.519 1.308-3.368 1.957-5.548.399-1.33.702-2.25.91-2.765.551-1.354 1.087-2.03 1.607-2.03.43 0 .732.217.91.652.22.527.444 1.782.67 3.766.123 1.005.331 2.211.625 3.62l.79 3.61c.82-1.972 1.847-4.64 3.077-8.001.068-.184.22-.763.46-1.737.177-.716.395-1.273.652-1.671.22-.337.508-.506.863-.506.619 0 1.643.43 1.643 1.043 0 .104-.813.286-1.009.794l-.367.993-.505 1.635-2.729 6.632c-.25.729-.683 1.788-1.295 3.178-.22.41-.551.616-.992.616z"></path></g><path d="M67.427 7.01a64.95 64.95 0 00-.211 5.107c0 .43.012.959.037 1.59.024.63.036 1.16.036 1.589-.623 1.156-1.85.737-2.112-.056.165-2.14.17-1.952.165-3.003 0-1.415.086-3.182.257-5.3.955-2.293 2.369-1.893 2.369-1.893.038.758-.579 1.553-.54 1.966zM67.077.33c2.337-.235 3.256 3.024 1.645 3.98-.912.54-2.076.252-2.835-.512-.473-.56-.589-.945-.47-1.564.201-1.047.88-1.826 1.66-1.904zm-.262 2.289c.156.58.551.714 1.043.355.48-.35.484-.858.007-1.167-.463-.3-1.198.267-1.05.812z"></path></g></svg></a><div class="jsx-4253649316 top-buttons"><div role="group" class="MuiButtonGroup-root MuiButtonGroup-contained css-8dr9ft"><button class="MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButtonBase-root Mui-disabled MuiButtonGroup-grouped MuiButtonGroup-groupedHorizontal MuiButtonGroup-groupedContained MuiButtonGroup-groupedContainedHorizontal MuiButtonGroup-groupedContainedPrimary css-1jc54ve" tabindex="-1" type="button" disabled=""><span class="MuiButton-startIcon MuiButton-iconSizeSmall css-u0g51i"><svg viewBox="0 0 24 24" role="presentation" style="width: 1.5rem; height: 1.5rem;"><path d="M15,9H5V5H15M12,19A3,3 0 0,1 9,16A3,3 0 0,1 12,13A3,3 0 0,1 15,16A3,3 0 0,1 12,19M17,3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V7L17,3Z" style="fill: currentcolor;"></path></svg></span><div class="PrivateHiddenCss-root PrivateHiddenCss-smDown css-1k0avvz">Save</div></button><button class="MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButtonBase-root jss4 MuiButtonGroup-grouped MuiButtonGroup-groupedHorizontal MuiButtonGroup-groupedContained MuiButtonGroup-groupedContainedHorizontal MuiButtonGroup-groupedContainedPrimary css-1jc54ve" tabindex="0" type="button"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="ArrowDropDownIcon"><path d="m7 10 5 5 5-5z"></path></svg><span class="MuiTouchRipple-root css-w0pj6f"></span></button></div><button class="MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButtonBase-root jss2 css-1jc54ve" tabindex="0" type="button"><span class="MuiButton-startIcon MuiButton-iconSizeSmall css-u0g51i"><svg viewBox="0 0 24 24" role="presentation" style="width: 1.5rem; height: 1.5rem;"><path d="M21,12L14,5V9C7,10 4,15 3,20C5.5,16.5 9,14.9 14,14.9V19L21,12Z" style="fill: currentcolor;"></path></svg></span>Share<span class="MuiTouchRipple-root css-w0pj6f"></span></button><button class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeLarge css-6ci2yv" tabindex="0" type="button" aria-label="Like this project"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FavoriteIcon"><path d="m12 21.35-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path></svg><span class="MuiTouchRipple-root css-w0pj6f"></span></button></div><div class="jsx-31981644 spacer"></div><nav class="jsx-31981644 menu"><a href="https://docs.wokwi.com/?utm_source=wokwi" target="_blank" class="jsx-31981644 docs-link">Docs</a></nav><button class="MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButtonBase-root css-1jc54ve" tabindex="0" type="button"><span class="user-menu_altContent__PHtj5"><span class="user-menu_alt1__swt4s">Sign in</span><span class="user-menu_alt2__U4wD7">Sign up</span></span><span class="MuiTouchRipple-root css-w0pj6f"></span></button></div></header><main class="jsx-4253649316"><div class="workbench-desktop_container__c61v2"><div class="sc-fujyUd jcalqq SplitPane vertical workbench-desktop_splitPane__B0r3f"><div class="sc-bdnylx dPXZpJ Pane vertical workbench-desktop_splitPane__B0r3f" style="flex-basis: 640px;"><div class="sc-dlnjPT hwITCb" style="background-color: black;"></div><div class="sc-gtssRu cuPrgG" style="min-width: 50px;"><div class="workbench-desktop_editor__L4Jxo"><div class="tabs_tabs__ztOIk"><button class="tabs_tab__iRWK_ tabs_active___gU2D tabs_errors__OLBf0">sketch.ino</button><button class="tabs_tab__iRWK_">diagram.json</button><button class="tabs_tab__iRWK_">Library Manager</button><button class="tabs_dropdown__xOoyW"><svg viewBox="0 0 24 24" role="presentation" style="width: 20px; height: 20px;"><path d="M7,10L12,15L17,10H7Z" style="fill: currentcolor;"></path></svg></button></div><div class="jsx-1496893965 editor-container" style=""><section class="code-editor_wrapper__AEiSo" style="display: flex; position: relative; text-align: initial; width: 100%; height: 100%;"><div data-keybinding-context="2" data-mode-id="arduino" style="width: 100%; --codelens-font-features_ee1f62:&quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="vfs:sketch.ino" style="width: 640px; height: 441px;"><div data-mprt="3" class="overflow-guard" style="width: 640px; height: 441px;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; height: 650px; width: 64px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 650px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute; width: 64px;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; width: 64px; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; height: 650px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:64px; height:19px;"></div><div class="active-line-number line-numbers" style="left:0px;width:38px;">1</div></div><div style="position: absolute; top: 114px; width: 100%; height: 19px;"><div class="line-numbers" style="left:0px;width:38px;">2</div></div><div style="position: absolute; top: 133px; width: 100%; height: 19px;"><div class="line-numbers" style="left:0px;width:38px;">3</div></div><div style="position: absolute; top: 152px; width: 100%; height: 19px;"><div class="line-numbers" style="left:0px;width:38px;">4</div></div><div style="position: absolute; top: 171px; width: 100%; height: 19px;"><div class="line-numbers" style="left:0px;width:38px;">5</div></div><div style="position: absolute; top: 190px; width: 100%; height: 19px;"><div class="line-numbers" style="left:0px;width:38px;">6</div></div><div style="position: absolute; top: 209px; width: 100%; height: 19px;"><div class="line-numbers" style="left:0px;width:38px;">7</div></div></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 64px; height: 441px; width: 576px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1e+06px; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; height: 0px; width: 576px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:576px; height:19px;"></div><div class="cdr  arrow-decoration-1" style="left:8px;width:0px;height:19px;"></div><div class="cdr squiggly-error" style="left:0px;width:31px;height:19px;"></div></div><div style="position: absolute; top: 114px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 133px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 152px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 171px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 190px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 209px; width: 100%; height: 19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute; width: 576px;"><div monaco-view-zone="e1" style="overflow: hidden; position: absolute; width: 100%; display: block; top: 19px; height: 95px;" monaco-visible-view-zone="true"></div></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; width: 576px; height: 650px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk1">from&nbsp;machine&nbsp;import&nbsp;Pin</span></span></div><div style="top: 114px; height: 19px;" class="view-line"><span><span class="mtk1">import&nbsp;utime</span></span></div><div style="top: 133px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 152px; height: 19px;" class="view-line"><span><span class="mtk1">led=Pin(</span><span class="mtk11">15</span><span class="mtk1">,Pin.OUT)</span></span></div><div style="top: 171px; height: 19px;" class="view-line"><span><span class="mtk10">while</span><span class="mtk1">&nbsp;True:</span></span></div><div style="top: 190px; height: 19px;" class="view-line"><span><span class="mtk1">led.toggle()</span></span></div><div style="top: 209px; height: 19px;" class="view-line"><span><span class="mtk1">utime.sleep(</span><span class="mtk11">0.5</span><span class="mtk1">)</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 562px; height: 12px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 12px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 562px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="21" height="661" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 441px;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical fade" style="position: absolute; width: 14px; height: 441px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 299px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 640px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="off" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; top: 0px; left: 64px; width: 1px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover line-numbers" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 640px;"><div class="accessibilityHelpWidget" role="dialog" aria-hidden="true" widgetid="editor.contrib.accessibilityHelpWidget" style="display: none; position: absolute;"><div role="document"></div></div><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div><div class="zone-widget" widgetid="vs.editor.contrib.zoneWidgete1" style="width: 626px; left: 0px; top: 19px; height: 95px; position: absolute;"><div class="zone-widget-container peekview-widget" style="border-top-color: rgb(229, 20, 0); border-bottom-color: rgb(229, 20, 0); height: 79px; border-top-width: 1px; border-bottom-width: 1px; top: 6px; overflow: hidden;"><div class="head" style="background-color: rgba(229, 20, 0, 0.1); height: 23px; line-height: 23px;"><div class="peekview-title"><div class="codicon codicon codicon-error"></div><span class="filename" title="sketch.ino" style="color: rgb(0, 0, 0);">sketch.ino</span><span class="dirname" style="color: rgb(97, 97, 97);">1 of 1 problem</span><span class="meta"></span></div><div class="peekview-actions"><div class="monaco-action-bar animated"><ul class="actions-container" role="toolbar"><li class="action-item menu-entry" role="presentation"><a class="action-label codicon codicon-marker-navigation-next" role="button" title="Go to Next Problem (Error, Warning, Info) (Alt+F8)"></a></li><li class="action-item menu-entry" role="presentation"><a class="action-label codicon codicon-marker-navigation-previous" role="button" title="Go to Next Problem (Error, Warning, Info) (Shift+Alt+F8)"></a></li><li class="action-item" role="presentation"><a class="action-label codicon codicon-close" role="button" title="Close" tabindex="0"></a></li></ul></div></div></div><div class="body marker-widget" tabindex="0" role="tooltip" style="background-color: rgb(255, 255, 254); border-color: rgb(229, 20, 0); height: 54px;"><div style="height: 54px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden; height: 54px; width: 626px;"><div class="descriptioncontainer" style="overflow: hidden; left: 0px; top: 0px;"><div class="message" aria-live="assertive" role="alert" aria-label="from machine import Pin, Error at 1:1. " style="font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px;"><div>'from' does not name a type; did you mean 'feof'?</div><div> feof</div></div><div style="font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 620px; height: 6px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 6px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 620px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 6px; height: 54px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 6px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 54px;"></div></div></div></div></div></div><div class="monaco-sash horizontal disabled" style="left: 0px; width: 640px; top: 85px;"></div></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 441px;"><div class="minimap-shadow-hidden" style="height: 441px;"></div><canvas width="0" height="661" style="position: absolute; left: 0px; width: 0px; height: 441px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="661" style="position: absolute; left: 0px; width: 0px; height: 441px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div></div><div data-mprt="2" class="overflowingContentWidgets"><div class="monaco-editor rename-box" widgetid="__renameInputWidget" style="background-color: rgb(243, 243, 243); box-shadow: rgba(0, 0, 0, 0.16) 0px 0px 8px 2px; color: rgb(97, 97, 97); position: absolute; display: none; visibility: hidden; max-width: 1280px;"><input class="rename-input" type="text" aria-label="Rename input. Type new name and press Enter to commit." style="font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; background-color: rgb(255, 255, 255); border-width: 0px; border-style: none;"><div class="rename-label" style="font-size: 11.2px;">Enter to Rename, Shift+Enter to Preview</div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip" widgetid="editor.contrib.modesContentHoverWidget" style="position: absolute; display: none; visibility: hidden; max-width: 1280px; top: 19px; left: 64px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-height: 250px; max-width: 500px;"><div class="hover-row"><div class="marker hover-contents" style="font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px;"><span style="white-space: pre-wrap;">'from' does not name a type; did you mean 'feof'?<br> feof</span></div></div><div class="hover-row status-bar"><div class="actions"><div class="action-container"><a class="action" role="button"><span>View Problem (Alt+F8)</span></a></div><div>No quick fixes available</div></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 383px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 383px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 10px; height: 69px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 69px;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div><div class="context-view" aria-hidden="true" style="display: none;"></div></div></div></section></div></div></div></div><div style="position: relative;"><div role="presentation" class="sc-jSFkmK hkrgyP Resizer vertical workbench-desktop_splitPane__B0r3f" style="width: 1rem;"><div class="sc-eCApGN kYDdaA"><div class="sc-iCoHVE knnrxv" style="flex-basis: 120px;"></div><div class="sc-hKFyIo bdDYJz" style="transform: scale(0); flex: 0 0 0px; position: relative; transition: transform 195ms cubic-bezier(0.4, 0, 0.2, 1) 0ms; visibility: hidden;"><button>➡</button></div><div class="sc-iCoHVE knnrxv" style="flex-basis: 80px;"></div></div></div><div class="sc-gKAblj lawQOz" style="opacity: 1; width: 1px; background-color: rgba(120, 120, 120, 0.3); transition: opacity 225ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;"></div><div class="sc-gKAblj lawQOz" style="opacity: 0; width: 4px; background: rgb(175, 82, 191); margin-left: -2px; transition: opacity 195ms cubic-bezier(0.4, 0, 0.2, 1) 0ms; visibility: hidden;"></div></div><div class="sc-bdnylx dPXZpJ Pane vertical workbench-desktop_splitPane__B0r3f" style="flex-basis: 640px;"><div class="sc-dlnjPT hwITCb" style="background-color: black;"></div><div class="sc-gtssRu cuPrgG" style="min-width: 50px;"><div class="workbench-desktop_preview__Eeuqi"><div class="tabs_tabs__ztOIk"><button class="tabs_tab__iRWK_ tabs_active___gU2D">Simulation</button></div><div class="jsx-3032653079 jss7"><div class="jsx-3032653079 simulation-controls"><div class="MuiBox-root css-1ynyhby"><button class="MuiButtonBase-root MuiFab-root MuiFab-circular MuiFab-sizeSmall MuiFab-secondary css-1jhqskv" tabindex="0" type="button" aria-label="Start the simulation" style="color: white;"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="PlayArrowIcon"><path d="M8 5v14l11-7z"></path></svg><span class="MuiTouchRipple-root css-w0pj6f"></span></button></div><div class="MuiBox-root css-1tanlhh"><button class="MuiButtonBase-root MuiFab-root MuiFab-circular MuiFab-sizeSmall MuiFab-primary css-1vjod7q" tabindex="0" type="button" aria-label="Add a new part"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="AddIcon"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></svg><span class="MuiTouchRipple-root css-w0pj6f"></span></button></div><div class="MuiBox-root css-1tanlhh"><button class="MuiButtonBase-root MuiFab-root MuiFab-circular MuiFab-sizeSmall css-auv765" tabindex="0" type="button" aria-label="Zoom, grid, and more" style="background: gray; color: white;"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="MoreVertIcon"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg><span class="MuiTouchRipple-root css-w0pj6f"></span></button></div></div><div class="diagram-viewer_viewer__AHflp"><div tabindex="0" style="cursor: pointer; flex: 1 1 0%;"><div style="transform-origin: 0px 0px 0px; transform: matrix(1.5, 0, 0, 1.5, 239.75, 92.2188); will-change: transform;"><div class="react-draggable" style="transform: translate(0px, 0px);"><wokwi-esp32-devkit-v1 class="diagram-part_diagramItem__ZeYe_ diagram-part_selectable__N65pi diagram-part_editMode__gIx0Q" id="esp" data-draggable="true" wokwi-controller="wokwi-esp32-devkit-v1" style="top: 0px; left: 0px; transform: rotate(0deg);"></wokwi-esp32-devkit-v1></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 154.5px; left: 1px;"><span>esp:VIN</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 145px; left: 1px;"><span>esp:GND.2</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 135.5px; left: 1px;"><span>esp:D13</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 126.4px; left: 1px;"><span>esp:D12</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 116px; left: 1px;"><span>esp:D14</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 106.8px; left: 1px;"><span>esp:D27</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 97px; left: 1px;"><span>esp:D26</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 87.3px; left: 1px;"><span>esp:D25</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 77.7px; left: 1px;"><span>esp:D33</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 68.2px; left: 1px;"><span>esp:D32</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 58.9px; left: 1px;"><span>esp:D35</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 49.1px; left: 1px;"><span>esp:D34</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 40px; left: 1px;"><span>esp:VN</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 30px; left: 1px;"><span>esp:VP</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 20px; left: 1px;"><span>esp:EN</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 154.5px; left: 97.3px;"><span>esp:3V3</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 145px; left: 97.3px;"><span>esp:GND.1</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 135.5px; left: 97.3px;"><span>esp:D15</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 126.4px; left: 97.3px;"><span>esp:D2</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 116px; left: 97.3px;"><span>esp:D4</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 106.8px; left: 97.3px;"><span>esp:RX2</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 97px; left: 97.3px;"><span>esp:TX2</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 87.3px; left: 97.3px;"><span>esp:D5</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 77.7px; left: 97.3px;"><span>esp:D18</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 68.2px; left: 97.3px;"><span>esp:D19</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 58.9px; left: 97.3px;"><span>esp:D21</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 49.1px; left: 97.3px;"><span>esp:RX0</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 40px; left: 97.3px;"><span>esp:TX0</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 30px; left: 97.3px;"><span>esp:D22</span></div><div data-draggable="0" class="diagram-part-pins_pinOverlay__It9jH" style="top: 20px; left: 97.3px;"><span>esp:D23</span></div><svg class="diagram-viewer_connections__0hy0c diagram-viewer_editMode__hgQxD" fill="none" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" viewBox="-2 -2 4 4" width="4" height="4" style="left: -2px; top: -2px;"></svg></div></div></div></div></div></div></div></div></div></main></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{}},"page":"/","query":{},"buildId":"QqMS8X537YjDwAEf_aVTK","runtimeConfig":{"PADDLE_SANDBOX":"0"},"nextExport":true,"autoExport":true,"isFallback":false,"scriptLoader":[]}</script><script src="./main_files/js" data-nscript="afterInteractive"></script><script id="google-analytics" data-nscript="afterInteractive">
          window.dataLayer = window.dataLayer || [];
          function gtag(){window.dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', 'UA-150413053-5');
        </script><next-route-announcer><p aria-live="assertive" id="__next-route-announcer__" role="alert" style="border: 0px; clip: rect(0px, 0px, 0px, 0px); height: 1px; margin: -1px; overflow: hidden; padding: 0px; position: absolute; width: 1px; white-space: nowrap; overflow-wrap: normal;">New ESP32 Project - Wokwi Simulator</p></next-route-announcer><script src="./main_files/[template]-b56b25b357bdbe2c.js.download"></script><div class="wokwi-elements-loaded" style="display: none;"></div><script src="./main_files/loader.js.download"></script><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><script src="./main_files/[share]-e4258d296f9dbbd6.js.download"></script></body></html>