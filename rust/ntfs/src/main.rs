extern crate winapi;

use std::ffi::OsString;
use std::os::windows::ffi::OsStringExt;
use std::ptr;
use winapi::shared::minwindef::{DWORD, FILETIME};
use winapi::um::fileapi::{CreateFileW, ReadFile};
use winapi::um::handleapi::CloseHandle;
use winapi::um::ioapiset::DeviceIoControl;
use winapi::um::winioctl::{FSCTL_GET_NTFS_VOLUME_DATA, NTFS_VOLUME_DATA_BUFFER};

fn main() {
    // Replace "path/to/your/forensic/image.dd" with the path to your NTFS forensic image file
    let image_path = r"/home/supato/images/ntfspaladin.001"; // Use the correct drive letter

    unsafe {
        let image_handle = CreateFileW(
            image_path.encode_wide().collect::<Vec<u16>>().as_ptr(),
            winapi::um::winnt::GENERIC_READ,
            winapi::um::fileapi::FILE_SHARE_READ | winapi::um::fileapi::FILE_SHARE_WRITE,
            ptr::null_mut(),
            winapi::um::fileapi::OPEN_EXISTING,
            winapi::um::fileapi::FILE_ATTRIBUTE_NORMAL,
            ptr::null_mut(),
        );

        if image_handle == winapi::um::handleapi::INVALID_HANDLE_VALUE {
            println!("Error opening file. Error code: {}", winapi::um::errhandlingapi::GetLastError());
            return;
        }

        let mut volume_data: NTFS_VOLUME_DATA_BUFFER = std::mem::zeroed();
        let mut bytes_read: DWORD = 0;

        let result = DeviceIoControl(
            image_handle,
            FSCTL_GET_NTFS_VOLUME_DATA,
            ptr::null_mut(),
            0,
            &mut volume_data as *mut _ as *mut std::ffi::c_void,
            std::mem::size_of_val(&volume_data) as DWORD,
            &mut bytes_read,
            ptr::null_mut(),
        );

        if result == 0 {
            println!("Error getting volume data. Error code: {}", winapi::um::errhandlingapi::GetLastError());
            CloseHandle(image_handle);
            return;
        }

        println!("Serial Number: {}", volume_data.VolumeSerialNumber);
        println!("Bytes Per Sector: {}", volume_data.BytesPerSector);
        println!("Total Clusters: {}", volume_data.TotalClusters);
        println!("Free Clusters: {}", volume_data.FreeClusters);

        CloseHandle(image_handle);
    }
}

