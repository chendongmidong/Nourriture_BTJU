package com.nourriture.app.setting;


import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import com.nourriture.app.R;

/**
 * Created by liuyifan on 15/12/10.
 */
public class PersonalSettingNameFragment extends Fragment {
    private View view;
    private String name;
    boolean isTwoPane;

    @Override
    public void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);

        //get name and isTwoPane from Bundle--tablet or Intent--phone
        if(getArguments()!=null && getArguments().containsKey("name") && getArguments().containsKey("isTwoPane")){
            name = getArguments().getString("name");
            isTwoPane = getArguments().getBoolean("isTwoPane");
        } else if(getActivity().getIntent().getStringExtra("name") != null){
            name = getActivity().getIntent().getStringExtra("name");
            isTwoPane = getActivity().getIntent().getBooleanExtra("isTwoPane", false);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        view = inflater.inflate(R.layout.setting_name_frag, container, false);

        setName(name);

        Button button = (Button) view.findViewById(R.id.name_submit);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view1) {
                EditText editText = (EditText) view.findViewById(R.id.edit_name);
                String name = editText.getText().toString();
                System.out.println("--Input:" + name);

                if(isTwoPane){
                    System.out.println("--Large:" + name);
                    // refresh the name value in the left fragment <TODO>
                } else {
                    System.out.println("--Small:" + name);
                    // close the activity and refresh the value <TODO>
                }
            }
        });
        return view;
    }

    // set the name into the EditText
    public void setName(String string){
        EditText nameView = (EditText) view.findViewById(R.id.edit_name);
        nameView.setText(string);
    }
}
