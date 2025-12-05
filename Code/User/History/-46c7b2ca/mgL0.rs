#![no_std]
#![no_main]
#![feature(abi_x86_interrupt)]

mod framebuffer;
mod interupts;

use core::panic::PanicInfo;
use bootloader_api::{BootInfo, entry_point, info::FrameBufferInfo};
use conquer_once::spin::OnceCell;
use bootloader_x86_64_common::logger::LockedLogger;
pub(crate) static LOGGER: OnceCell<LockedLogger> = OnceCell::uninit();


#[panic_handler]
fn panic(info: &PanicInfo) -> ! {
    let loc = info.location().unwrap();
    log::error!("PANIC@{:?}:{:?} in {:?} {:?}", loc.line(), loc.column(), loc.file(), info.message());
    loop {}
}


fn init_logger_stage_1(boot_info: &'static mut BootInfo) {
    let frame_buffer_optional = &mut boot_info.framebuffer;
    let frame_buffer_option = frame_buffer_optional.as_mut();
    let frame_buffer_struct = frame_buffer_option.unwrap();
    let frame_buffer_info = frame_buffer_struct.info().clone();
    let raw_frame_buffer = frame_buffer_struct.buffer_mut();
    init_logger_stage_2(raw_frame_buffer, frame_buffer_info);
}

pub(crate) fn init_logger_stage_2(buffer: &'static mut [u8], info: FrameBufferInfo) {
    let logger = LOGGER.get_or_init(move || LockedLogger::new(buffer, info, true, false));
    log::set_logger(logger).expect("Logger already set");
    log::set_max_level(log::LevelFilter::Trace);
}


fn init_logger(boot_info: &'static mut BootInfo) {
    init_logger_stage_1(boot_info);
}

fn init_subsystems() {
    interupts::init_idt();
}

entry_point!(kernel_main);

fn kernel_main(boot_info: &'static mut BootInfo) -> ! {
    
    init_logger(boot_info);
    init_subsystems();
    loop {}
}

