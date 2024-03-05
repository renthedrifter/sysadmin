use ntfs_forensics::{MftReader, Record};
use std::fs::File;
use std::io::{self, Read, Seek, SeekFrom};

fn main() -> io::Result<()> {
    // Replace "path/to/your/forensic/image.dd" with the path to your NTFS forensic image file
    let image_path = "path/to/your/forensic/image.dd";

    let mut image_file = File::open(image_path)?;
    let mut mft_reader = MftReader::new(&mut image_file)?;

    // Iterate over MFT records and display metadata
    while let Some(record) = mft_reader.next()? {
        display_metadata(&record);
    }

    Ok(())
}

fn display_metadata(record: &Record) {
    // Display basic file metadata
    println!("File Name: {}", record.get_file_name().unwrap_or("Unknown"));
    println!("File Size: {} bytes", record.get_file_size());
    println!("Creation Time: {:?}", record.get_creation_time());
    println!("Modified Time: {:?}", record.get_last_data_change_time());
    println!("Access Time: {:?}", record.get_last_access_time());
    println!("File Attributes: {:?}", record.get_file_attributes());
    println!("-----------------------------");
}


