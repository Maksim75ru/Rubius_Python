from Storage import *
from FileManager import FileManager


if __name__ == '__main__':
    main_storage: ReadOnlyStorage = ReadWriteStorage("~/data_storage")

    personal_file_manager = FileManager('personal', main_storage)
    personal_file_manager.add_file(File(0, "user_1", "file_1"))
    personal_file_manager.add_file(File(1, "user_2", "file_2"))
    print(personal_file_manager.get_all_files())

    work_files_manager = FileManager('work', main_storage)

    f = File(1, "user_1", "file_2")
    print(f.data)
    work_files_manager.add_file(f)
    print(work_files_manager.get_all_files())

    # Тесты
    tmp_storage = ReadOnlyStorage("/tmp/tests/data_storage")
    # assert len(tmp_storage.get_all()) == 0
    tmp_storage.get_one(1)
    # tmp_storage.delete_one(1)
